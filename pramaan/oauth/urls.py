from django.urls import path
from oauth.views import (
    oauth_dashboard_view,
    oauth_branding_view,
    oauth_client_view,
    client_detail_view,
    oauth_delete_view,
    oauth_verification_view,
)

app_name = "oauth"

urlpatterns = [
    path("", oauth_dashboard_view, name="oauth"),
    path("branding/", oauth_branding_view, name="branding"),
    path("client/", oauth_client_view, name="client"),
    path("detail/<int:pk>", client_detail_view, name="client-detail"),
    path("delete/<int:pk>", oauth_delete_view, name="client-delete"),
    path("verification/", oauth_verification_view, name="verification"),
]
