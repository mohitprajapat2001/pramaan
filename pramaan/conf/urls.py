from django.contrib import admin
from django.urls import path, include
from conf.routers import router
from django.conf import settings
from django.conf.urls.static import static

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
    path("oauth/", include("oauth.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
