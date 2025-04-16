from django.views.generic import TemplateView
from utils.constants import Templates
from utils.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = Templates.DASHBOARD_TEMPLATE


dashboard_view = DashboardView.as_view()
