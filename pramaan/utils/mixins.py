from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from utils.constants import Messages


class MessageMixin:
    """
    override default get_success_url method to add message in response
    """

    success_message = None
    message_level = messages.SUCCESS

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_message:
            messages.add_message(self.request, self.message_level, self.success_message)
        return response


class LoginRequiredMixin:
    """
    Custom login validator class to override default dispatch method
    """

    url = reverse_lazy("accounts:login")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.url)
        return super().dispatch(request, *args, **kwargs)


class OAuthBaseMixin:
    """
    override dispatch method to check where query params have oauth id else redirect to user's oauth dashboard
    """

    def dispatch(self, request, *args, **kwargs):
        if request.GET.get("oauth"):
            return super().dispatch(request, *args, **kwargs)
        if oauth := request.user.oauths.first():
            return redirect(reverse_lazy(self.url) + "?oauth=%s" % oauth.id)
        messages.add_message(request, messages.INFO, Messages.OAUTH_NOT_IN_QUERY_PARAMS)
        return redirect(reverse_lazy("oauth:oauth"))


class BaseMultipleFormView(View):
    success_url = reverse_lazy("landing:home")
    message_level = messages.SUCCESS
    success_message = None

    def get(self, request, *args, **kwargs):
        return redirect(self.success_url)

    def success_url_redirect(self):
        if self.success_message:
            messages.add_message(
                request=self.request,
                level=self.message_level,
                message=self.success_message,
            )
        return redirect(self.success_url)
