from django.urls import path
from accounts.views import (
    login_view,
    logout_view,
    register_view,
    profile_view,
    address_view,
    social_view,
    detail_view,
    emergency_view,
)


app_name = "accounts"

urlpatterns = (
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("address/", address_view, name="address"),
    path("social/", social_view, name="social"),
    path("detail/", detail_view, name="detail"),
    path("emergency/", emergency_view, name="emergency"),
)
