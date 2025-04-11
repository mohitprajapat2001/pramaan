from django.utils.translation import gettext_lazy as _


class Labels:
    """Account app form label"""

    EMAIL = _("Email")
    PASSWORD = _("Password")


class Placeholders:
    """Account app form placeholder"""

    EMAIL = _("Please enter your email")
    PASSWORD = _("Please enter your password")


class SucccessMessages:
    """Accounts app success message"""

    LOGIN_SUCCESS = _("Logged in successfully")
    LOGOUT_SUCCESS = _("Logout successfully")


class ValidationErrors:
    """Account app validation errors"""

    INVALID_EMAIL_PASSWORD = _("Invalid email or password")
    INVALID_CREDENTIALS = _("Invalid Credentials")
