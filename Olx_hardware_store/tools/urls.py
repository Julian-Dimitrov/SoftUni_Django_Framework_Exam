from django.urls import path, include
from .views import add_tool, DetailsToolView, EditToolView, DeleteToolView


urlpatterns = [
    path('add/', add_tool, name="add_tool"),
    path('<str:username>/tool/<slug:slug>/', include([
        path('', DetailsToolView.as_view(), name="details_tool"),
        path('edit/', EditToolView.as_view(), name="edit_tool"),
        path('delete/', DeleteToolView.as_view(), name="delete_tool"),
    ])),
]
