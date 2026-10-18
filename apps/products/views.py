from django.views.generic import TemplateView
from apps.products.services import get_home_page_data


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            get_home_page_data()
        )
        return context