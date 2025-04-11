from django.views.generic import View, FormView
from utils.constants import Templates
from accounts.constants import SucccessMessages, ValidationErrors
from accounts.forms import LoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.messages import info
from django.shortcuts import redirect
from django.forms import ValidationError
from django.contrib.auth import authenticate


class LoginView(FormView, SuccessMessageMixin):
    """Pramaan Default Login View"""

    template_name = Templates.LOGIN_TEMPLATE
    form_class = LoginForm
    success_url = reverse_lazy("landing:home")
    success_message = SucccessMessages.LOGIN_SUCCESS

    def form_valid(self, form):
        user = authenticate(**form.cleaned_data)
        if not user:
            raise ValidationError({"password": ValidationErrors.INVALID_EMAIL_PASSWORD})
        login(self.request, user)
        return super().form_valid(form)


login_view = LoginView.as_view()


class LogoutView(View):
    success_url = reverse_lazy("landing:home")
    success_message = SucccessMessages.LOGOUT_SUCCESS

    """Pramaan Default Logout View"""

    def get(self, request, *args, **kwargs):
        logout(request)
        info(request=request, message=self.success_message)
        return redirect(self.success_url)


logout_view = LogoutView.as_view()
