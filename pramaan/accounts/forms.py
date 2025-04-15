from django.forms import (
    Form,
    ModelForm,
    EmailField,
    PasswordInput,
    EmailInput,
    CharField,
    TextInput,
    ValidationError,
    URLInput,
    DateInput,
    NumberInput,
    Select,
    Textarea,
)
from utils.utils import get_model
from utils.constants import AppModel, FormClass
from django.contrib.auth.password_validation import validate_password
from accounts.constants import (
    Labels,
    Placeholders,
    ValidationErrors,
)

User = get_model(**AppModel.USER)
UserDetail = get_model(**AppModel.USER_DETAIL)
SocialAccounts = get_model(**AppModel.SOCIAL_ACCOUNTS)
Address = get_model(**AppModel.ADDRESS)


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


class SocialAccountsForm(ModelForm):
    """Social Accounts Form"""

    class Meta:
        model = SocialAccounts
        fields = (
            "facebook",
            "instagram",
            "twitter",
            "linkedin",
            "youtube",
            "github",
            "website",
            "tiktok",
        )
        widgets = {}
        labels = {}
        for field in fields:
            class_name = FormClass.TEXT_INPUT
            widgets[field] = URLInput(
                attrs={
                    "class": class_name,
                    "placeholder": Placeholders.SOCIAL_ACCOUNT[field],
                }
            )
            labels[field] = Labels.SOCIAL_ACCOUNT[field]


class UserDetailForm(ModelForm):
    """User Detail Form"""

    class Meta:
        model = UserDetail
        fields = (
            "secondary_email",
            "phone_number",
            "secondary_phone_number",
            "date_of_birth",
            "gender",
            "marrital_status",
            "bio",
        )
        widgets = {}
        labels = {}
        for field in fields:
            class_name = FormClass.TEXT_INPUT
            input_type = EmailInput
            if field == "date_of_birth":
                widgets[field] = DateInput(
                    attrs={
                        "class": class_name,
                        "placeholder": Placeholders.USER_DETAIL[field],
                        "type": "date",
                    }
                )
            elif field in ("phone_number", "secondary_phone_number"):
                input_type = NumberInput
            elif field in ("gender", "marrital_status"):
                input_type = Select
            elif field == "bio":
                input_type = Textarea
                class_name = FormClass.TEXTAREA
            if not field == "date_of_birth":
                widgets[field] = input_type(
                    attrs={
                        "class": class_name,
                        "placeholder": Placeholders.USER_DETAIL[field],
                    }
                )
            labels[field] = Labels.USER_DETAIL[field]


class AddressForm(ModelForm):
    """Address Form"""

    class Meta:
        model = Address
        fields = (
            "address_line_1",
            "address_line_2",
            "city",
            "pincode",
            "address_type",
        )
        widgets = {}
        labels = {}
        for field in fields:
            if field == "form":
                continue
            class_name = FormClass.TEXT_INPUT
            input_type = TextInput
            if field == "pincode":
                input_type = NumberInput
            elif field in ("address_type", "city"):
                input_type = Select
                class_name = FormClass.SELECT_INPUT if field == "address_type" else ""
            widgets[field] = input_type(
                attrs={
                    "class": class_name,
                    "placeholder": Placeholders.ADDRESS[field],
                }
            )
            labels[field] = Labels.ADDRESS[field]
