from django.urls import reverse_lazy
from django.views import generic as views
from Olx_hardware_store.tools.models import Tool
from .forms import SearchForm


class ListToolsView(views.ListView):
    template_name = 'common/main_page.html'
    model = Tool
    paginate_by = 4
    ordering = ['-created_on', ]

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_authenticated:
            queryset = queryset.exclude(user=self.request.user)

        search = self.request.GET.get('search', '')
        filter_field = self.request.GET.get('filter_field')

        if filter_field == 'name':
            queryset = queryset.filter(name__icontains=search)
        elif filter_field == 'tool_country':
            queryset = queryset.filter(tool_country__icontains=search)
        else:
            queryset = queryset.filter(tool_city__icontains=search)

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['form'] = SearchForm(
            initial={
                'search': self.request.GET.get('search', ''),
                'filter_field': self.request.GET.get('filter_field', '')
            }
        )
        return context


class ClearSearchView(views.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        redirect_url = reverse_lazy('main_page')

        return redirect_url
