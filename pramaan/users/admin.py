from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from utils.utils import get_model
from utils.constants import AppModel

User = get_model(**AppModel.USER)
UserDetail = get_model(**AppModel.USER_DETAIL)
Profile = get_model(**AppModel.PROFILE)
Address = get_model(**AppModel.ADDRESS)
SocialAccounts = get_model(**AppModel.SOCIAL_ACCOUNTS)
EmergencyDetails = get_model(**AppModel.EMERGENCY_DETAILS)
SecurityQuestion = get_model(**AppModel.SECURITY_QUESTION)
Subscription = get_model(**AppModel.SUBSCRIPTION)


class UserDetailInline(admin.StackedInline):
    model = UserDetail
    can_delete = False
    verbose_name_plural = "User Details"
    fk_name = "user"
    extra = 1


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profiles"
    fk_name = "user"
    extra = 1


class AddressInline(admin.StackedInline):
    model = Address
    can_delete = True
    verbose_name_plural = "Addresses"
    fk_name = "user"
    extra = 1


class SocialAccountsInline(admin.StackedInline):
    model = SocialAccounts
    can_delete = False
    verbose_name_plural = "Social Accounts"
    fk_name = "user"
    extra = 1


class EmergencyDetailsInline(admin.StackedInline):
    model = EmergencyDetails
    can_delete = True
    verbose_name_plural = "Emergency Details"
    fk_name = "user"
    extra = 1


class SecurityQuestionInline(admin.StackedInline):
    model = SecurityQuestion
    can_delete = True
    verbose_name_plural = "Security Questions"
    fk_name = "user"
    extra = 1


class SubscriptionInline(admin.StackedInline):
    model = Subscription
    can_delete = False
    verbose_name_plural = "Subscription"
    fk_name = "user"
    extra = 1


@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [
        UserDetailInline,
        ProfileInline,
        AddressInline,
        SocialAccountsInline,
        EmergencyDetailsInline,
        SecurityQuestionInline,
        SubscriptionInline,
    ]

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "status",
        "date_joined",
    )
    search_fields = ("email", "username", "first_name", "last_name")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Status", {"fields": ("status",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
