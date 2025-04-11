from django.forms import (
    Form,
    EmailField,
    PasswordInput,
    EmailInput,
    CharField,
)
from utils.utils import get_model
from utils.constants import AppModel, FormClass
from accounts.constants import Labels, Placeholders

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
