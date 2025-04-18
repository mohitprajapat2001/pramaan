from utils.utils import get_model
from utils.constants import AppModel, FormClass
from django import forms
from oauth.constants import PlaceHolders, Labels


Oauth = get_model(**AppModel.OAUTH)
Client = get_model(**AppModel.CLIENT)
AuthorizedDomains = get_model(**AppModel.AUTHORIZED_DOMAINS)
RedirectURIs = get_model(**AppModel.REDIRECT_URIS)


class OAuthForm(forms.ModelForm):
    class Meta:
        model = Oauth
        fields = (
            "title",
            "description",
            "support_email",
            "logo",
            "app_domain",
            "app_terms_of_service",
            "app_privacy_policy",
            "developer_email",
        )
        widgets = {}
        labels = {}
        for field in fields:
            input_type = forms.URLInput
            class_type = FormClass.TEXT_INPUT
            if field == "logo":
                input_type = forms.ClearableFileInput
                class_type = FormClass.FILE_INPUT
            elif field == "status":
                input_type = forms.Select
                class_type = FormClass.SELECT_INPUT
            elif field in ("support_email", "developer_email"):
                input_type = forms.EmailInput
            elif field == "title":
                input_type = forms.TextInput
                class_type = FormClass.TEXT_INPUT
            elif field == "description":
                input_type = forms.TextInput
                class_type = FormClass.TEXTAREA
            widgets[field] = input_type(
                attrs={"class": class_type, "placeholder": PlaceHolders.OAUTH[field]}
            )
            labels[field] = Labels.OAUTH[field]


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ("title", "description")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": FormClass.TEXT_INPUT,
                    "placeholder": PlaceHolders.CLIENT["title"],
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": FormClass.TEXTAREA,
                    "placeholder": PlaceHolders.CLIENT["description"],
                }
            ),
        }
        labels = {
            "title": Labels.CLIENT["title"],
            "description": Labels.CLIENT["description"],
        }
