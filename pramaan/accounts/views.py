from django.views.generic import View, FormView, TemplateView
from utils.constants import Templates, AppModel
from accounts.constants import (
    SucccessMessages,
    ValidationErrors,
    ADDRESS_FORM,
    USER_DETAIL_FORM,
    SOCIAL_FORM,
    EMERGENCY_FORM,
)
from accounts.forms import (
    LoginForm,
    RegisterForm,
    AddressForm,
    SocialAccountsForm,
    UserDetailForm,
    EmergencyDetailsForm,
)
from django.contrib.messages.views import SuccessMessageMixin
from utils.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from utils.utils import get_model
from accounts.form_mixins import BaseMultipleFormView
from typing import Any

SocialAccounts = get_model(**AppModel.SOCIAL_ACCOUNTS)


class LoginView(SuccessMessageMixin, FormView):
    """Pramaan Default Login View"""

    template_name = Templates.LOGIN_TEMPLATE
    form_class = LoginForm
    success_url = reverse_lazy("landing:home")
    success_message = SucccessMessages.LOGIN_SUCCESS

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        if not user:
            form.add_error("password", ValidationErrors.INVALID_CREDENTIALS)
            return self.form_invalid(form)
        login(self.request, user)
        return super().form_valid(form)


login_view = LoginView.as_view()


class LogoutView(LoginRequiredMixin, View):
    success_url = reverse_lazy("landing:home")
    success_message = SucccessMessages.LOGOUT_SUCCESS

    """Pramaan Default Logout View"""

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request=request, message=self.success_message)
        return redirect(self.success_url)


logout_view = LogoutView.as_view()


class RegisterationView(SuccessMessageMixin, FormView):
    template_name = Templates.REGISTER_TEMPLATE
    success_url = reverse_lazy("accounts:login")
    success_message = SucccessMessages.REGISTER_SUCCESS
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        form.save()
        return super().form_valid(form)


register_view = RegisterationView.as_view()


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = Templates.PROFILE_TEMPLATE

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["social_form"] = SocialAccountsForm(
            instance=self.request.user.social_accounts
        )
        context["detail_form"] = UserDetailForm(instance=self.request.user.detail)
        context["form"] = AddressForm()
        context["emergency_form"] = EmergencyDetailsForm()
        context["action"] = {
            "social": SOCIAL_FORM,
            "detail": USER_DETAIL_FORM,
            "address": ADDRESS_FORM,
            "emergency": EMERGENCY_FORM,
        }
        return context


profile_view = ProfileView.as_view()


class AddressView(BaseMultipleFormView):
    form_class = AddressForm
    success_url = reverse_lazy("accounts:profile")
    success_message = SucccessMessages.ADDRESS_SUCCESS

    def get(self, request, *args, **kwargs):
        if self.request.GET.get("id"):
            address = self.request.user.addresses.filter(
                id=self.request.GET.get("id")
            ).first()
            if not address:
                self.success_message = SucccessMessages.ADDRESS_NOT_FOUND
                self.message_level = messages.ERROR
                return self.success_url_redirect()
            address.delete()
            self.success_message = SucccessMessages.ADDRESS_DELETED
            self.message_level = messages.SUCCESS
        return self.success_url_redirect()

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=self.request.POST)
        if not form.is_valid():
            for field, error in form.errors.items():
                messages.error(self.request, error)
            return self.form_invalid(form)
        form.save(commit=False)
        form.instance.user = self.request.user
        form.save()
        return self.success_url_redirect()


address_view = AddressView.as_view()


class SocialView(BaseMultipleFormView):
    form_class = SocialAccountsForm
    success_url = reverse_lazy("accounts:profile")
    success_message = SucccessMessages.SOCIAL_UPDATED

    def post(self, request, *args, **kwargs):
        form = self.form_class(
            instance=self.request.user.social_accounts, data=self.request.POST
        )
        if not form.is_valid():
            for field, error in form.errors.items():
                messages.error(self.request, error)
            return self.form_invalid(form)
        form.save()
        return self.success_url_redirect()


social_view = SocialView.as_view()


class DetailView(BaseMultipleFormView):
    form_class = UserDetailForm
    success_url = reverse_lazy("accounts:profile")
    success_message = SucccessMessages.UPDATE_SUCCESS

    def post(self, request, *args, **kwargs):
        form = self.form_class(
            instance=self.request.user.detail, data=self.request.POST
        )
        if not form.is_valid():
            for field, error in form.errors.items():
                messages.error(self.request, error)
            return self.form_invalid(form)
        form.save()
        if data := self.request.POST:
            if last_name := data.get("last_name"):
                self.request.user.last_name = last_name
            elif first_name := data.get("first_name"):
                self.request.user.first_name = first_name
            self.request.user.save()
        return self.success_url_redirect()


detail_view = DetailView.as_view()


class EmergencyView(BaseMultipleFormView):
    form_class = EmergencyDetailsForm
    success_url = reverse_lazy("accounts:profile")
    success_message = SucccessMessages.EMERGENCY_SUCCESS

    def get(self, request, *args, **kwargs):
        if self.request.GET.get("id"):
            address = self.request.user.emergency_details.filter(
                id=self.request.GET.get("id")
            ).first()
            if not address:
                self.success_message = SucccessMessages.EMERGENCY_CONTACT_NOT_FOUND
                self.message_level = messages.ERROR
                return self.success_url_redirect()
            address.delete()
            self.success_message = SucccessMessages.EMERGENCY_CONTACT_DELETED
            self.message_level = messages.SUCCESS
        return self.success_url_redirect()

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=self.request.POST)
        if not form.is_valid():
            for field, error in form.errors.items():
                messages.error(self.request, error)
            return self.form_invalid(form)
        form.save(commit=False)
        form.instance.user = request.user
        form.save()
        return self.success_url_redirect()


emergency_view = EmergencyView.as_view()
