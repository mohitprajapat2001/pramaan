from django.views.generic import TemplateView
from utils.constants import Templates


class LandingView(TemplateView):
    template_name = Templates.LANDING


landing_view = LandingView.as_view()
