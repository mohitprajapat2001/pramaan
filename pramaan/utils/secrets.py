import random
import string
from utils.utils import get_model
from utils.constants import AppModel
from django.db.models.fields import Field


def generate_client_id():
    """
    Generate Unique Client ID
    constraints
    1. 8 characters
    2. Numeric
    """
    Client = get_model(**AppModel.CLIENT)
    while True:
        client_id = "".join(random.choices(string.digits, k=8))
        if not Client.objects.filter(client_id=client_id).exists():
            return client_id


def generate_client_secret():
    """
    Generate Unique Client Secret
    constraints
    1. 32 characters
    2. Alphanumeric
    """
    Client = get_model(**AppModel.CLIENT)
    while True:
        client_secret = generate_random_string()
        if not Client.objects.filter(client_secret=client_secret).exists():
            return client_secret


class ClientId(Field):
    """Custom field to generate unique client id"""

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 6
        kwargs["unique"] = True
        super().__init__(*args, **kwargs)

    def pre_save(self, instance, add):
        value = getattr(instance, self.attname)
        if not value:
            value = generate_client_id()
            setattr(instance, self.attname, value)
        return value


class ClientSecret(Field):
    """Custom field to generate unique client secret"""

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 6
        kwargs["unique"] = True
        super().__init__(*args, **kwargs)

    def pre_save(self, instance, add):
        value = getattr(instance, self.attname)
        if not value:
            value = generate_client_secret()
            setattr(instance, self.attname, value)
        return value


def generate_random_string():
    """
    Generate Random String
    """
    return "".join(random.choices(string.printable, k=32))
