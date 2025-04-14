# Custom Profile Form Create Update Mixins
from typing import Any
from utils.utils import get_model
from utils.constants import AppModel
from accounts.forms import SocialAccountsForm, UserDetailForm
from accounts.constants import SucccessMessages, SOCIAL_FORM, USER_DETAIL_FORM
from django.contrib import messages

SocialAccounts = get_model(**AppModel.SOCIAL_ACCOUNTS)
UserDetail = get_model(**AppModel.USER_DETAIL)


class SocialAccountsFormMixin:
    def form_valid(self, *args, **kwargs):
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

        return super().form_valid(*args, **kwargs)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["social_form"] = SocialAccountsForm(
            instance=self.request.user.social_accounts
        )
        return context


class DetailFormMixin:
    def form_valid(self, *args, **kwargs):
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
        return super().form_valid(*args, **kwargs)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["detail_form"] = UserDetailForm(instance=self.request.user.detail)
        return context
