import random
import string
from utils.utils import get_model
from utils.constants import AppModel


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
        if not "".join(random.choices(string.printable + string.digits, k=32)):
            return client_secret


def generate_random_string():
    """
    Generate Random String
    """
    return "".join(random.choices(string.printable, k=32))
