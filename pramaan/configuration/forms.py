from utils.utils import get_model
from utils.constants import AppModel, FormClass
from django import forms
from configuration.constants import PlaceHolders, Labels

UserPreference = get_model(**AppModel.USER_PREFERENCE)
Notification = get_model(**AppModel.NOTIFICATION)
NotificationPreference = get_model(**AppModel.NOTIFICATION_PREFERENCE)
UserPrivacySettings = get_model(**AppModel.USER_PRIVACY_SETTINGS)


class UserPreferenceForm(forms.ModelForm):
    class Meta:
        model = UserPreference
        fields = ["theme"]
        widgets = {
            "theme": forms.Select(
                attrs={
                    "class": FormClass.SELECT_INPUT + " max-w-3xs",
                    "placeholder": PlaceHolders.THEME,
                }
            )
        }
        labels = {"theme": Labels.THEME}


class NotificationPreferenceForm(forms.ModelForm):
    class Meta:
        model = NotificationPreference
        fields = ("is_enabled",)
        widgets = {
            "is_enabled": forms.CheckboxInput(
                attrs={
                    "class": FormClass.SWITCH_INPUT,
                    "placeholder": PlaceHolders.NOTIFICATIONS,
                }
            )
        }
        labels = {"is_enabled": Labels.NOTIFICATIONS}


class UserPrivacySettingsForm(forms.ModelForm):
    class Meta:
        model = UserPrivacySettings
        fields = ("show_email", "show_phone", "allow_messages")
        widgets = {}
        labels = {}
        for field in fields:
            widgets[field] = forms.CheckboxInput(
                attrs={
                    "class": FormClass.SWITCH_INPUT,
                    "placeholder": PlaceHolders.PRIVACY[field],
                }
            )
            labels[field] = Labels.PRIVACY[field]
