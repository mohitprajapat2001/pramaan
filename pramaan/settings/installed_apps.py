THIRD_PARTY_APPS = [
    "rest_framework",
    "django_extensions",
    "corsheaders",
    "cities_light",
    "rest_framework_simplejwt",
    "phonenumber_field",
    "django_rq",
]


PROJECT_APPS = [
    "users.apps.UsersConfig",
    "configuration.apps.ConfigurationConfig",
    "dashboard.apps.DashboardConfig",
    "oauth.apps.OauthConfig",
]
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
INSTALLED_APPS = THIRD_PARTY_APPS + PROJECT_APPS + DJANGO_APPS
