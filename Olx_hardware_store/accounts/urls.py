from django.urls import path, include
from .views import RegisterUserView, LoginUserView, LogoutUserView, ProfileDetailsView, ProfileEditView,\
    ProfileDeleteView, add_phone_numbers, ForbiddenView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='details_profile'),
        path('edit/', ProfileEditView.as_view(), name='edit_profile'),
        path('delete/', ProfileDeleteView.as_view(), name='delete_profile'),
        path('contacts/', include([
            path('', add_phone_numbers, name='contacts_profile')
        ]))
    ])),
    path('403/', ForbiddenView.as_view(), name='forbidden')
]

# admin user juli21
# password for all users 123$QWEr
