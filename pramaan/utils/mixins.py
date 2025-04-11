from django.contrib.messages import info
from django.urls import reverse_lazy
from django.shortcuts import redirect


class MessageMixin:
    """
    override default get_success_url method to add message in response
    """

    success_message = None

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_message:
            info(self.request, self.success_message)
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
