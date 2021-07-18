from users.forms import CreateUserForm
from django.urls import path
from users.views import ListUsersView, CreateUserView


urlpatterns = [
    path('', ListUsersView.as_view(), name='users'),
    path('create/', CreateUserView.as_view(), name='create'),
]
