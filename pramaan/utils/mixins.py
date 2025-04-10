from django.contrib.messages import info


class MessageMixin:
    """
    override default get_success_url method to add message in response
    """

    success_message = None

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_message:
            info(self.request, self.success_message)
        return response
