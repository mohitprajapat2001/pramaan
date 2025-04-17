from django.views.generic import TemplateView
from utils.mixins import LoginRequiredMixin, OAuthBaseMixin
from utils.constants import Templates, AppModel
from oauth.constants import PageTitles
from typing import Any
from oauth.forms import OAuthForm, ClientForm
from utils.utils import get_model

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


class OAuthClientView(LoginRequiredMixin, OAuthBaseMixin, TemplateView):
    template_name = Templates.OAUTH_CLIENT_TEMPLATE
    url = "oauth:client"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # context["create_client_form"] = ClientForm()
        context["page_title"] = PageTitles.CLIENT
        return context

    def post(self, request, *args, **kwargs):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        return self.post(request, *args, **kwargs)


oauth_client_view = OAuthClientView.as_view()


class OAuthVerificationView(LoginRequiredMixin, OAuthBaseMixin, TemplateView):
    template_name = Templates.OAUTH_VERIFICATION_TEMPLATE
    url = "oauth:verification"


oauth_verification_view = OAuthVerificationView.as_view()
