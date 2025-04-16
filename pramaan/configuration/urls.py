from django.urls import path
from configuration.views import configuration_view

app_name = "configuration"


urlpatterns = [
    path("", configuration_view, name="configuration"),
]
