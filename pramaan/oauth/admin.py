from utils.utils import get_model
from utils.constants import AppModel

from django.contrib import admin


Oauth = get_model(**AppModel.OAUTH)
Client = get_model(**AppModel.CLIENT)
AuthorizedDomains = get_model(**AppModel.AUTHORIZED_DOMAINS)
RedirectURIs = get_model(**AppModel.REDIRECT_URIS)


class AuthrizedDomainsInline(admin.StackedInline):
    model = AuthorizedDomains
    extra = 0


class RedirectURIsInline(admin.StackedInline):
    model = RedirectURIs
    extra = 0


@admin.register(Oauth)
class OauthAdmin(admin.ModelAdmin):
    inlines = [AuthrizedDomainsInline, RedirectURIsInline]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
