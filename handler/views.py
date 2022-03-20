from api.serializers import CsrSerializer
from django.views.generic import TemplateView
from handler.mixins import Fetcher


class CsrListView(Fetcher, TemplateView):
    """List view of Csrs."""

    template_name = 'handler/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = 'https://spending.gov.ru/api/budget/csrref?page=1&page_size=10'
        context['csrs'] = self.exceptions_handler(self.fetch_objects)(url, CsrSerializer)
        return context
