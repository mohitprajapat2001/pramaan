from django.utils.translation import gettext_lazy as _

SOCIAL_FORM = "accounts:social"
ADDRESS_FORM = "accounts:address"
USER_DETAIL_FORM = "accounts:detail"
EMERGENCY_FORM = "accounts:emergency"


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

    EMERYGENCY_DETAILS = {
        "name": "Name",
        "phone_number": "Phone Number",
        "relationship": "Relationship",
    }

    PASSWORD_CHANGE = {
        "old_password": "Old Password",
        "password": "New Password",
        "confirm_password": "Confirm Password",
    }
    USERNAME_CHANGE = {
        "username": "Username",
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
    EMERYGENCY_DETAILS = {
        "name": "Name",
        "phone_number": "Phone Number",
        "relationship": "Relationship",
    }

    PASSWORD_CHANGE = {
        "old_password": "Old Password",
        "password": "New Password",
        "confirm_password": "Confirm Password",
    }
    USERNAME_CHANGE = {
        "username": "Username",
    }


class SucccessMessages:
    """Accounts app success message"""

    LOGIN_SUCCESS = _("Logged in successfully")
    LOGOUT_SUCCESS = _("Logout successfully")
    REGISTER_SUCCESS = _("Registered successfully")
    PROFILE_SUCCESS = _("Profile updated successfully")
    UPDATE_SUCCESS = _("Updated successfully")
    ADDRESS_SUCCESS = _("Address added successfully")
    SOCIAL_UPDATED = _("Social accounts updated successfully")
    ADDRESS_DELETED = _("Address deleted successfully")
    ADDRESS_UPDATED = _("Address updated successfully")
    ADDRESS_NOT_FOUND = _("Address not found")
    EMERGENCY_SUCCESS = _("Emergency details added successfully")
    EMERGENCY_CONTACT_NOT_FOUND = _("Emergency contact not found")
    EMERGENCY_CONTACT_DELETED = _("Emergency contact deleted successfully")
    PASSWORD_CHANGED = _("Password changed successfully")
    USERNAME_CHANGED = _("Username changed successfully")


class ValidationErrors:
    """Account app validation errors"""

    INVALID_EMAIL_PASSWORD = _("Invalid email or password")
    INVALID_CREDENTIALS = _("Invalid Credentials")
    PASSWORD_MISMATCH = _("Password mismatch")
    LOGIN_REQUIRED = _("Please login to access this page")
    SAME_PASSWORD = _("Old and new password cannot be same")
    USERNAME_NOT_AVAILABLE = _("Username not available")
    INCORRECT_PASSWORD = _("Incorrect password")
