from django.views.generic import View, FormView
from utils.constants import Templates, AppModel
from accounts.constants import SucccessMessages, ValidationErrors
from accounts.forms import LoginForm, RegisterForm, AddressForm
from django.contrib.messages.views import SuccessMessageMixin
from utils.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from utils.utils import get_model
from accounts.form_mixins import SocialAccountsFormMixin, DetailFormMixin

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


class ProfileBaseViewMixin(SocialAccountsFormMixin, DetailFormMixin):
    invalid_error_url = reverse_lazy("accounts:profile")

    def add_message(self):
        messages.add_message(self.request, self.message_level, self.success_message)


class ProfileView(
    ProfileBaseViewMixin,
    LoginRequiredMixin,
    SuccessMessageMixin,
    FormView,
):
    template_name = Templates.PROFILE_TEMPLATE
    form_class = AddressForm
    success_url = reverse_lazy("accounts:profile")
    success_message = SucccessMessages.ADDRESS_SUCCESS

    def form_valid(self, form):
        address = form.save(commit=False)
        address.user = self.request.user
        form.save()
        return super().form_valid(form)


profile_view = ProfileView.as_view()
