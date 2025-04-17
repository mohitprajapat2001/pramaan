from django.urls import path
from oauth.views import (
    oauth_dashboard_view,
    oauth_branding_view,
    oauth_client_view,
    oauth_verification_view,
)

app_name = "oauth"

urlpatterns = [
    path("", oauth_dashboard_view, name="oauth"),
    path("branding/", oauth_branding_view, name="branding"),
    path("client/", oauth_client_view, name="client"),
    path("verification/", oauth_verification_view, name="verification"),
]
