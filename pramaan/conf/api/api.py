from users.choices import (
    GenderChoices,
    RelationshipChoices,
    QuestionChoices,
    AccountStatus,
    SubscriptionPlans,
    MarritialStatus,
    AddressType,
)
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from http import HTTPStatus


class StaticBaseApi(ListModelMixin, GenericViewSet):
    choice_name = None
    serializer_class = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.choice_name:
            raise ValueError("choice_name must be set")

    def get_queryset(self):
        return [
            {"value": key, "text": value} for key, value in self.choice_name.CHOICES
        ]

    def list(self, request, *args, **kwargs):
        return Response(self.get_queryset(), status=HTTPStatus.OK)


class GenderApi(StaticBaseApi):
    choice_name = GenderChoices


class RelationshipApi(StaticBaseApi):
    choice_name = RelationshipChoices


class QuestionApi(StaticBaseApi):
    choice_name = QuestionChoices


class AccountStatusApi(StaticBaseApi):
    choice_name = AccountStatus


class SubscriptionPlansApi(StaticBaseApi):
    choice_name = SubscriptionPlans


class MarritialStatusApi(StaticBaseApi):
    choice_name = MarritialStatus


class AddressTypeApi(StaticBaseApi):
    choice_name = AddressType
