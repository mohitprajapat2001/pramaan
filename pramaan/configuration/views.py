from django.views.generic import TemplateView
from utils.constants import Templates


class ConfigurationView(TemplateView):
    template_name = Templates.CONFIGURATION


configuration_view = ConfigurationView.as_view()
