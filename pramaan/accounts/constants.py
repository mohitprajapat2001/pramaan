from django.utils.translation import gettext_lazy as _


class Labels:
    """Account app form label"""

    EMAIL = _("Email")
    PASSWORD = _("Password")

    REGISTER = {
        "email": "Email",
        "password": "Password",
        "confirm_password": "Confirm Password",
    }


class Placeholders:
    """Account app form placeholder"""

    EMAIL = _("Please enter your email")
    PASSWORD = _("Please enter your password")

    REGISTER = {
        "email": "Please enter your email",
        "password": "Please enter your password",
        "confirm_password": "Please confirm your password",
    }


class SucccessMessages:
    """Accounts app success message"""

    LOGIN_SUCCESS = _("Logged in successfully")
    LOGOUT_SUCCESS = _("Logout successfully")
    REGISTER_SUCCESS = _("Registered successfully")
    PROFILE_SUCCESS = _("Profile updated successfully")


class ValidationErrors:
    """Account app validation errors"""

    INVALID_EMAIL_PASSWORD = _("Invalid email or password")
    INVALID_CREDENTIALS = _("Invalid Credentials")
    PASSWORD_MISMATCH = _("Password mismatch")
    LOGIN_REQUIRED = _("Please login to access this page")
