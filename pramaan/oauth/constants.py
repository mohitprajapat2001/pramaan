from django.utils.translation import gettext_lazy as _

OAUTH_LOGO_UPLOAD_PATH = "oauth/%s/%s"


class OauthStatusChoices:
    """Ouath App Oauth Model status Choices"""

    TESTING = "testing"
    PRODUCTION_NOT_VERIFIED = "production_unverified"
    PRODUCTION_VERIFIED = "production_verified"

    CHOICES = (
        (TESTING, _("Testing")),
        (PRODUCTION_NOT_VERIFIED, _("Production Unverified")),
        (PRODUCTION_VERIFIED, _("Production Verified")),
    )


class PageTitles:
    """OAuth App Page Titles"""

    OVERVIEW = _("Overview")
    BRANDING = _("Branding")
