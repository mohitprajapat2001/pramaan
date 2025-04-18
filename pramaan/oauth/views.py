from django.views.generic import TemplateView, FormView, DeleteView, DetailView
from utils.mixins import LoginRequiredMixin, OAuthBaseMixin
from django.contrib.messages.views import SuccessMessageMixin
from utils.constants import Templates, AppModel, Messages
from oauth.constants import PageTitles
from typing import Any
from oauth.forms import OAuthForm, ClientForm
from utils.utils import get_model
from django.urls import reverse_lazy
from django_extensions.db.models import ActivatorModel
from django.shortcuts import redirect
from django.contrib import messages

Oauth = get_model(**AppModel.OAUTH)
Client = get_model(**AppModel.CLIENT)
AuthorizedDomains = get_model(**AppModel.AUTHORIZED_DOMAINS)
RedirectURIs = get_model(**AppModel.REDIRECT_URIS)


class OAuthDashboardView(LoginRequiredMixin, TemplateView):
    template_name = Templates.OAUTH_TEMPLATE

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["page_title"] = PageTitles.OVERVIEW
        return context


oauth_dashboard_view = OAuthDashboardView.as_view()


class OAuthBrandingView(LoginRequiredMixin, OAuthBaseMixin, TemplateView):
    template_name = Templates.OAUTH_BRANDING_TEMPLATE
    url = "oauth:branding"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        id = self.request.GET.get("oauth")
        if oauth := self.request.user.oauths.filter(id=id).first():
            context["oauth"] = oauth
        else:
            context["oauth"] = self.request.user.oauths.first()
        context["oauth_form"] = OAuthForm(instance=context["oauth"])
        context["page_title"] = PageTitles.BRANDING
        return context

    def post(self, request, *args, **kwargs):
        id = self.request.GET.get("oauth")
        if oauth := self.request.user.oauths.filter(id=id).first():
            form = OAuthForm(request.POST, request.FILES, instance=oauth)
            if form.is_valid():
                form.save()
            if form.errors:
                print(form.errors)
        return self.get(request, *args, **kwargs)


oauth_branding_view = OAuthBrandingView.as_view()


class OAuthClientView(
    LoginRequiredMixin, OAuthBaseMixin, SuccessMessageMixin, FormView
):
    template_name = Templates.OAUTH_CLIENT_TEMPLATE
    url = "oauth:client"
    form_class = ClientForm
    success_url = reverse_lazy("oauth:client")
    success_message = Messages.CLIENT_CREATED

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        id = self.request.GET.get("oauth")
        if oauth := self.request.user.oauths.filter(id=id).first():
            context["oauth"] = oauth
        else:
            context["oauth"] = self.request.user.oauths.first()
        context["page_title"] = PageTitles.CLIENT
        return context

    def form_valid(self, form):
        form.instance.oauth = self.request.user.oauths.first()
        form.save()
        self.success_url = reverse_lazy(
            "oauth:client-detail", kwargs={"pk": form.instance.id}
        )
        return super().form_valid(form)


oauth_client_view = OAuthClientView.as_view()


class ClientDetailView(LoginRequiredMixin, DetailView):
    queryset = Client.objects.all()
    template_name = Templates.CLIENT_DETAIL_TEMPLATE
    context_object_name = "client"

    def get(self, request, *args, **kwargs):
        client = super().get_object(self.queryset)
        if client.status == ActivatorModel.ACTIVE_STATUS:
            messages.add_message(
                self.request, messages.INFO, Messages.CLIENT_VIEW_ONCE_EXPIRED
            )
            return redirect(reverse_lazy("oauth:client"))
        client.status = ActivatorModel.ACTIVE_STATUS
        client.save(update_fields=("status",))
        return super().get(request, *args, **kwargs)


client_detail_view = ClientDetailView.as_view()


class OAuthDeleteView(SuccessMessageMixin, DeleteView):
    queryset = Client.objects.filter(status=ActivatorModel.ACTIVE_STATUS)
    success_url = reverse_lazy("oauth:client")
    success_message = Messages.CLIENT_DELETED


oauth_delete_view = OAuthDeleteView.as_view()


class OAuthVerificationView(LoginRequiredMixin, OAuthBaseMixin, TemplateView):
    template_name = Templates.OAUTH_VERIFICATION_TEMPLATE
    url = "oauth:verification"


oauth_verification_view = OAuthVerificationView.as_view()
