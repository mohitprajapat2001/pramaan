from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel,
)
from oauth.constants import OAUTH_LOGO_UPLOAD_PATH, OauthStatusChoices
from utils.secrets import ClientId, ClientSecret


def _oauth_logo_path(self, filename):
    """
    Path to save the oauth logo.
    """
    return OAUTH_LOGO_UPLOAD_PATH % (self.id, filename)


class Oauth(TimeStampedModel, ActivatorModel, TitleDescriptionModel):
    """
    Oauth model
    """

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="oauths"
    )
    support_email = models.EmailField(verbose_name="Support Email")
    logo = models.ImageField(
        upload_to=_oauth_logo_path, blank=True, null=True, verbose_name="Logo"
    )
    developer_email = models.EmailField(
        verbose_name="Developer Email", null=True, blank=True
    )
    app_domain = models.URLField(verbose_name="App Domain")
    app_privacy_policy = models.URLField(
        verbose_name="App Privacy Policy", null=True, blank=True
    )
    app_terms_of_service = models.URLField(
        verbose_name="App Terms of Service", null=True, blank=True
    )
    status = models.CharField(
        choices=OauthStatusChoices.CHOICES,
        default=OauthStatusChoices.TESTING,
        verbose_name="Publishing Status",
        max_length=32,
    )


class Client(TitleDescriptionModel, ActivatorModel, TimeStampedModel):
    """
    Client model
    """

    oauth = models.ForeignKey(Oauth, on_delete=models.CASCADE, related_name="clients")
    client_id = ClientId()
    client_secret = ClientSecret()
    status = models.IntegerField(
        choices=ActivatorModel.STATUS_CHOICES, default=ActivatorModel.INACTIVE_STATUS
    )


class AuthorizedDomains(ActivatorModel, TimeStampedModel):
    """
    Authorized Domains
    """

    oauth = models.ForeignKey(
        Oauth, on_delete=models.CASCADE, related_name="authorized_domains"
    )
    domain = models.URLField(verbose_name="Domain")


class RedirectURIs(ActivatorModel, TimeStampedModel):
    """
    Redirect URIs
    """

    client = models.ForeignKey(
        Oauth, on_delete=models.CASCADE, related_name="redirect_uris"
    )
    redirect_uri = models.URLField(verbose_name="Redirect URI")
