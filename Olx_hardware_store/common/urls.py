from django.urls import path
from .views import ToolsListView

urlpatterns = [
    path('', ToolsListView.as_view(), name='main_page'),
]
