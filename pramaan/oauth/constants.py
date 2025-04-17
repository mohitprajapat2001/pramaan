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


class PlaceHolders:
    """OAuth App PlaceHolders"""

    # OAuth
    OAUTH = {
        "title": _("Title"),
        "description": _("Description"),
        "support_email": _("Support Email"),
        "logo": _("Logo"),
        "app_domain": _("App Domain"),
        "app_terms_of_service": _("App Terms of Service"),
        "app_privacy_policy": _("App Privacy Policy"),
        "developer_email": _("Developer Email"),
    }


class Labels:
    """OAuth App Labels"""

    # OAuth
    OAUTH = {
        "title": _(
            """
    <h1 class="text-xl">
        App Name
    </h1>
    <p class="text-xs text-light italic">
        The name of the app asking for consent
    </p>
"""
        ),
        "description": _(
            """
    <h1 class="text-xl">
        App Description
    </h1>
    <p class="text-xs text-light italic">
        A short description of the app asking for consent
    </p>
"""
        ),
        "support_email": _(
            """
    <h1 class="text-xl">
        Support Email
    </h1>
    <p class="text-xs text-light italic">
        For users to contact you with questions about consent screen.
        <a href="" class="text-secondary">Learn more <i class="fa fa-up-right-from-square"></i></a>
    </p>
"""
        ),
        "logo": _(
            """
    <h1 class="text-xl">
        App Logo
    </h1>
    <p>
        This is your logo. It helps people to recognise your app and is displayed on the OAuth consent screen.
        After you upload a logo, you will need to submit your app for verification unless the app is configured for internal use only or has a publishing status of 'Testing'.
        <a href="" class="text-secondary">Learn more <i class="fa fa-up-right-from-square"></i></a>
    </p>
"""
        ),
        "app_domain": _(
            """
    <h1 class="text-xl">
        App Domain
    </h1>
    <p>
       To protect you and your users, Pramaan only allows apps using OAuth to use Authorised Domains. The following information will be shown to your users on the consent screen.
    <p>
"""
        ),
        "app_terms_of_service": _(
            """
                                   <h1 class="text-xl">
                                  App Terms of Service
    </h1>
                                  """
        ),
        "app_privacy_policy": _(
            """
                                   <h1 class="text-xl">
            App Privacy Policy
    </h1>
                                  """
        ),
        "developer_email": _(
            """
    <h1 class="text-xl">
        Developer Email
    </h1>
    <p class="text-xs  text-light italic">
    These email addresses are for Pramaan to notify you about any changes to your project.
    <p>
"""
        ),
    }
