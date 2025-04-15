# Custom Profile Form Create Update Mixins
from typing import Any
from utils.utils import get_model
from utils.constants import AppModel
from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from accounts.forms import SocialAccountsForm, UserDetailForm
from accounts.constants import SucccessMessages, SOCIAL_FORM, USER_DETAIL_FORM
from django.contrib import messages

SocialAccounts = get_model(**AppModel.SOCIAL_ACCOUNTS)
UserDetail = get_model(**AppModel.USER_DETAIL)


class SocialAccountsFormMixin:
    def post(self, request, *args, **kwargs):
        """
        SocialAccounts Form Update handling
        """
        if self.request.POST.get("form") == SOCIAL_FORM:
            form = SocialAccountsForm(
                data=self.request.POST, instance=self.request.user.social_accounts
            )
            if not form.is_valid():
                for field, error in form.errors.items():
                    self.message_level = messages.ERROR
                    self.success_message = error
                return self.form_invalid(form)
            form.save()
            self.success_message = SucccessMessages.UPDATE_SUCCESS

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["social_form"] = SocialAccountsForm(
            instance=self.request.user.social_accounts
        )
        return context


class DetailFormMixin:
    def post(self, *args, **kwargs):
        """
        SocialAccounts Form Update handling
        """
        if self.request.POST.get("form") == USER_DETAIL_FORM:
            form = UserDetailForm(
                data=self.request.POST, instance=self.request.user.detail
            )
            if not form.is_valid():
                for field, error in form.errors.items():
                    self.message_level = messages.ERROR
                    self.success_message = error
                return self.form_invalid(form)
            form.save()
            if data := self.request.POST:
                if last_name := data.get("last_name"):
                    self.request.user.last_name = last_name
                if first_name := data.get("first_name"):
                    self.request.user.first_name = first_name
                self.request.user.save()
            self.success_message = SucccessMessages.UPDATE_SUCCESS

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["detail_form"] = UserDetailForm(instance=self.request.user.detail)
        return context


class BaseMultipleFormView(View):
    success_url = reverse_lazy("landing:home")
    message_level = messages.SUCCESS
    success_message = None

    def success_url_redirect(self):
        if self.success_message:
            messages.add_message(
                request=self.request,
                level=self.message_level,
                message=self.success_message,
            )
        return redirect(self.success_url)
