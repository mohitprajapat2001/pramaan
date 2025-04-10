from django.views.generic import FormView
from utils.constants import Templates
from accounts.constants import SucccessMessages
from accounts.forms import LoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class LoginView(FormView, SuccessMessageMixin):
    template_name = Templates.LOGIN_TEMPLATE
    form_class = LoginForm
    success_url = reverse_lazy("landing:home")
    success_message = SucccessMessages.LOGIN_SUCCESS


login_view = LoginView.as_view()
