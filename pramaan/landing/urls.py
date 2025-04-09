from django.urls import path
from landing.views import landing_view

app_name = "landing"
urlpatterns = [
    path("", landing_view, name="home"),
]
