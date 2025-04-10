from django.forms import (
    Form,
    EmailField,
    PasswordInput,
    EmailInput,
    CharField,
    ValidationError,
)
from utils.utils import get_model
from utils.constants import AppModel, FormClass
from accounts.constants import Labels, Placeholders, ValidationErrors
from django.contrib.auth import authenticate

User = get_model(**AppModel.USER)


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

    def clean(self):
        cleaned_data = super().clean()
        user = authenticate(**cleaned_data)
        if not user:
            raise ValidationError({"password": ValidationErrors.INVALID_EMAIL_PASSWORD})
        return cleaned_data
