from django.utils.translation import gettext_lazy as _

SOCIAL_FORM = "social_form"
ADDRESS_FORM = "address_form"
USER_DETAIL_FORM = "user_detail_form"


class Labels:
    """Account app form label"""

    EMAIL = _("Email")
    PASSWORD = _("Password")

    REGISTER = {
        "email": "Email",
        "password": "Password",
        "confirm_password": "Confirm Password",
    }

    SOCIAL_ACCOUNT = {
        "facebook": "Facebook",
        "instagram": "Instagram",
        "twitter": "Twitter",
        "linkedin": "Linkedin",
        "youtube": "Youtube",
        "github": "Github",
        "website": "Website",
        "tiktok": "Tiktok",
    }
    USER_DETAIL = {
        "secondary_email": "Secondary Email",
        "phone_number": "Phone Number",
        "secondary_phone_number": "Secondary Phone Number",
        "date_of_birth": "Date of Birth",
        "gender": "Gender",
        "marrital_status": "Marrital Status",
        "bio": "Bio",
    }

    ADDRESS = {
        "address_line_1": "Address Line 1",
        "address_line_2": "Address Line 2",
        "city": "City",
        "pincode": "Pincode",
        "address_type": "Address Type",
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

    SOCIAL_ACCOUNT = {
        "facebook": "Facebook",
        "instagram": "Instagram",
        "twitter": "Twitter",
        "linkedin": "Linkedin",
        "youtube": "Youtube",
        "github": "Github",
        "website": "Website",
        "tiktok": "Tiktok",
    }

    USER_DETAIL = {
        "secondary_email": "Secondary Email",
        "phone_number": "Phone Number",
        "secondary_phone_number": "Secondary Phone Number",
        "date_of_birth": "Date of Birth",
        "gender": "Gender",
        "marrital_status": "Marrital Status",
        "bio": "Bio",
    }
    ADDRESS = {
        "address_line_1": "Address Line 1",
        "address_line_2": "Address Line 2",
        "city": "City",
        "pincode": "Pincode",
        "address_type": "Address Type",
    }


class SucccessMessages:
    """Accounts app success message"""

    LOGIN_SUCCESS = _("Logged in successfully")
    LOGOUT_SUCCESS = _("Logout successfully")
    REGISTER_SUCCESS = _("Registered successfully")
    PROFILE_SUCCESS = _("Profile updated successfully")
    UPDATE_SUCCESS = _("Updated successfully")
    ADDRESS_SUCCESS = _("Address added successfully")


class ValidationErrors:
    """Account app validation errors"""

    INVALID_EMAIL_PASSWORD = _("Invalid email or password")
    INVALID_CREDENTIALS = _("Invalid Credentials")
    PASSWORD_MISMATCH = _("Password mismatch")
    LOGIN_REQUIRED = _("Please login to access this page")
