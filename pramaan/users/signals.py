from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.utils import get_model
from utils.constants import AppModel

User = get_model(**AppModel.USER)
UserDetail = get_model(**AppModel.USER_DETAIL)
SocialAccounts = get_model(**AppModel.SOCIAL_ACCOUNTS)
EmergencyDetails = get_model(**AppModel.EMERGENCY_DETAILS)
Subscription = get_model(**AppModel.SUBSCRIPTION)

EMAIL_BASED_USERNAME_EXIST = "%s%s"


@receiver(post_save, sender=User)
def create_user_detail(sender, instance, created, **kwargs):
    if created:
        # Update username field based on email
        email = instance.email.split("@")[0]
        instance.username = EMAIL_BASED_USERNAME_EXIST % (email, instance.id)
        instance.save(update_fields=["username"])
        # Create UserDetail
        UserDetail.objects.create(user=instance)
        # Create SocialAccounts
        SocialAccounts.objects.create(user=instance)
        # Create Subscription
        Subscription.objects.create(user=instance)
