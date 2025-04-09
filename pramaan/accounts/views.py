from django.views.generic import TemplateView
from utils.constants import Templates


class LoginView(TemplateView):
    template_name = Templates.LOGIN_TEMPLATE


login_view = LoginView.as_view()
