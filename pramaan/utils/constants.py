from django.utils.translation import gettext_lazy as _

DD_MM_YYYY = "%d-%m-%Y"
YYYY_MM_DD = "%Y-%m-%d"


class Settings:
    """Settings Constants"""

    ROOT_URLCONF = "conf.urls"
    AUTH_USER_MODEL = "users.User"
    WSGI_APPLICATION = "conf.wsgi.application"
    ASGI_APPLICATION = "conf.asgi.application"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    USE_I18N = True
    USE_TZ = True
    STATIC_URL = "static/"
    STATIC_ROOT = "assets/"
    STATIC_FILES_DIRS = "static/"
    TEMPLATES_URLS = "templates/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media/"
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


class EmailConfig:
    """Email Configurations"""

    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    PORT_465 = 465
    PORT_587 = 587


class CacheTimeout:
    ONE_MINUTE = 60
    TEN_MINUTES = 60 * 10
    THIRTY_MINUTES = 60 * 30
    ONE_HOUR = 60 * 60
    ONE_DAY = 60 * 60 * 24
    ONE_WEEK = 60 * 60 * 24 * 7

    @classmethod
    def x_minutes(cls, x: int):
        return x * 60


class Templates:
    LANDING = "landing/home.html"
    LOGIN_TEMPLATE = "accounts/login.html"
    REGISTER_TEMPLATE = "accounts/register.html"
    PROFILE_TEMPLATE = "accounts/profile.html"
    ACCOUNT_TEMPLATE = "accounts/accounts.html"
    # Configuration App
    CONFIGURATION = "configuration/configuration.html"
    # Dashboard App
    DASHBOARD_TEMPLATE = "dashboard/dashboard.html"
    # OAuth App
    OAUTH_TEMPLATE = "oauth/pages/overview.html"
    OAUTH_BRANDING_TEMPLATE = "oauth/pages/branding.html"
    OAUTH_CLIENT_TEMPLATE = "oauth/pages/client.html"
    CLIENT_DETAIL_TEMPLATE = "oauth/pages/client-detail.html"
    OAUTH_VERIFICATION_TEMPLATE = "oauth/pages/verification.html"
    OAUTH_VALIDATION_TEMPLATE = "oauth/pages/validation.html"


class AppModel:
    USER = {
        "app_label": "users",
        "model_name": "User",
    }
    USER_DETAIL = {
        "app_label": "users",
        "model_name": "UserDetail",
    }
    PROFILE = {
        "app_label": "users",
        "model_name": "Profile",
    }
    ADDRESS = {
        "app_label": "users",
        "model_name": "Address",
    }
    SOCIAL_ACCOUNTS = {
        "app_label": "users",
        "model_name": "SocialAccounts",
    }
    EMERGENCY_DETAILS = {
        "app_label": "users",
        "model_name": "EmergencyDetails",
    }
    SECURITY_QUESTION = {
        "app_label": "users",
        "model_name": "SecurityQuestion",
    }
    SUBSCRIPTION = {
        "app_label": "users",
        "model_name": "Subscription",
    }
    # Configuration App Models
    USER_PREFERENCE = {
        "app_label": "configuration",
        "model_name": "UserPreference",
    }
    NOTIFICATION = {
        "app_label": "configuration",
        "model_name": "Notification",
    }
    NOTIFICATION_PREFERENCE = {
        "app_label": "configuration",
        "model_name": "NotificationPreference",
    }
    USER_PRIVACY_SETTINGS = {
        "app_label": "configuration",
        "model_name": "UserPrivacySettings",
    }
    # OAuth App Models
    OAUTH = {
        "app_label": "oauth",
        "model_name": "Oauth",
    }
    CLIENT = {
        "app_label": "oauth",
        "model_name": "Client",
    }
    AUTHORIZED_DOMAINS = {
        "app_label": "oauth",
        "model_name": "AuthorizedDomains",
    }
    REDIRECT_URIS = {
        "app_label": "oauth",
        "model_name": "RedirectURIs",
    }


class FormClass:
    TEXT_INPUT = "validator input w-full input-primary"
    FILE_INPUT = "validator file-input w-full file-input-primary"
    SELECT_INPUT = "validator select w-full select-primary"
    TEXTAREA = "textarea validator w-full textarea-primary"
    SWITCH_INPUT = "toggle toggle-primary"
    CHECKBOX_INPUT = "checkbox w-full checkbox-primary"


class Messages:
    OAUTH_NOT_IN_QUERY_PARAMS = _("OAuth id not found in query params")
    CLIENT_CREATED = _("Client created successfully")
    CLIENT_UPDATED = _("Client updated successfully")
    CLIENT_DELETED = _("Client deleted successfully")
    CLIENT_VIEW_ONCE_EXPIRED = _("Client view once link expired")
