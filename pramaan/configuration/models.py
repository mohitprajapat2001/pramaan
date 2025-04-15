from django.db import models
from django_extensions.db.models import TimeStampedModel, ActivatorModel
from configuration.constants import ThemeChoice


class UserPreference(TimeStampedModel):
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="preferences"
    )
    theme = models.CharField(
        max_length=20, choices=ThemeChoice.THEME_CHOICES, default=ThemeChoice.DARK
    )

    class Meta:
        verbose_name = "User Preference"
        verbose_name_plural = "User Preferences"

    def __str__(self):
        return self.user


class Notification(TimeStampedModel, ActivatorModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="notifications"
    )
    title = models.CharField(max_length=255, help_text="Title of the notification.")
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return self.user


class NotificationPreference(TimeStampedModel):
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="notification_preferences"
    )
    is_enabled = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Notification Preference"
        verbose_name_plural = "Notification Preferences"

    def __str__(self):
        return self.user


class UserPrivacySettings(models.Model):
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="privacy"
    )
    show_email = models.BooleanField(
        default=False, help_text="Allow others to see the user's email."
    )
    show_phone = models.BooleanField(
        default=False, help_text="Allow others to see the user's phone number."
    )
    allow_messages = models.BooleanField(
        default=True, help_text="Allow others to send messages to the user."
    )

    def __str__(self):
        return f"Privacy Settings for {self.user.username}"
