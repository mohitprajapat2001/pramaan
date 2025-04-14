from django.forms import (
    Form,
    ModelForm,
    EmailField,
    PasswordInput,
    EmailInput,
    CharField,
    TextInput,
    ValidationError,
)
from utils.utils import get_model
from utils.constants import AppModel, FormClass
from django.contrib.auth.password_validation import validate_password
from accounts.constants import Labels, Placeholders, ValidationErrors

User = get_model(**AppModel.USER)
UserDetail = get_model(**AppModel.USER_DETAIL)
SocialAccounts = get_model(**AppModel.SOCIAL_ACCOUNTS)


class RegisterForm(ModelForm):
    """Accounts Default Registeration Form"""

    confirm_password = CharField(
        max_length=16,
        required=True,
        widget=PasswordInput(
            attrs={
                "placeholder": Placeholders.REGISTER["confirm_password"],
                "class": FormClass.TEXT_INPUT,
            }
        ),
        label=Labels.REGISTER["confirm_password"],
    )

    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {}
        labels = {}
        for field in fields:
            class_name = FormClass.TEXT_INPUT
            field_type = TextInput
            if field == "email":
                field_type = EmailInput
            elif field == "password":
                field_type = PasswordInput
            widgets[field] = field_type(
                attrs={"class": class_name, "placeholder": Placeholders.REGISTER[field]}
            )
            labels[field] = Labels.REGISTER[field]

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise ValidationError(
                {"confirm_password": ValidationErrors.PASSWORD_MISMATCH}
            )
        return cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get("password")
        validate_password(password)
        return password


class LoginForm(Form):
    email = EmailField(
        max_length=32,
        widget=EmailInput(
            attrs={"placeholder": Placeholders.EMAIL, "class": FormClass.TEXT_INPUT}
        ),
        label=Labels.EMAIL,
        required=True,
    )
    password = CharField(
        max_length=16,
        widget=PasswordInput(
            attrs={"placeholder": Placeholders.PASSWORD, "class": FormClass.TEXT_INPUT}
        ),
        label=Labels.PASSWORD,
        required=True,
    )


class ProfileDetailForm(ModelForm):
    class Meta:
        model = UserDetail
        fields = []


class SocialAccountsForm(ModelForm):
    class Meta:
        model = SocialAccounts
        fields = (
            "facebook",
            "twitter",
            "instagram",
        )
