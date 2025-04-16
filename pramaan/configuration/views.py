from django.views.generic import TemplateView
from utils.constants import Templates
from configuration.constants import SucccessMessages
from configuration.forms import (
    UserPreferenceForm,
    NotificationPreferenceForm,
    UserPrivacySettingsForm,
)
from utils.mixins import LoginRequiredMixin, BaseMultipleFormView
from typing import Any
from django.urls import reverse_lazy


class ConfigurationView(LoginRequiredMixin, TemplateView, BaseMultipleFormView):
    template_name = Templates.CONFIGURATION
    success_message = SucccessMessages.CONFIGURATIONS_UPDATE
    success_url = reverse_lazy("configuration:configuration")

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["preference_form"] = UserPreferenceForm(
            instance=self.request.user.preferences
        )
        context["notification_form"] = NotificationPreferenceForm(
            instance=self.request.user.notification_preferences
        )
        context["privacy_form"] = UserPrivacySettingsForm(
            instance=self.request.user.privacy
        )
        return context

    def post(self, request, *args, **kwargs):
        preferences = UserPreferenceForm(
            request.POST, instance=request.user.preferences
        )
        notifications = NotificationPreferenceForm(
            request.POST, instance=request.user.notification_preferences
        )
        privacy = UserPrivacySettingsForm(request.POST, instance=request.user.privacy)
        if preferences.is_valid() and notifications.is_valid() and privacy.is_valid():
            preferences.save()
            notifications.save()
            privacy.save()
        return self.success_url_redirect()


configuration_view = ConfigurationView.as_view()
