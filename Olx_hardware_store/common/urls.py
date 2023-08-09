from django.urls import path
from .views import ListToolsView

urlpatterns = [
    path('', ListToolsView.as_view(), name='main_page'),
]
