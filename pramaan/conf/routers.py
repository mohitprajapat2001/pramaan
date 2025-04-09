from rest_framework.routers import DefaultRouter
from conf.api.api import (
    GenderApi,
    RelationshipApi,
    QuestionApi,
    AccountStatusApi,
    SubscriptionPlansApi,
    MarritialStatusApi,
    AddressTypeApi,
)


router = DefaultRouter()

router.register("gender", GenderApi, basename="gender")
router.register("relationship", RelationshipApi, basename="relationship")
router.register("question", QuestionApi, basename="question")
router.register("account-status", AccountStatusApi, basename="account-status")
router.register(
    "subscription-plans", SubscriptionPlansApi, basename="subscription-plans"
)
router.register("marritial-status", MarritialStatusApi, basename="marritial-status")
router.register("address-type", AddressTypeApi, basename="address-type")
