from django.contrib import admin
from django.urls import path, include
from conf.routers import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/",
        include(router.urls),
    ),
    path("", include("landing.urls")),
    path("accounts/", include("accounts.urls")),
    path("configuration/", include("configuration.urls")),
    path("dashboard/", include("dashboard.urls")),
]
