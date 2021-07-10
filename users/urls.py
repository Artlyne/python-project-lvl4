from django.urls import path
from users.views import UsersListView

urlpatterns = [
    path('', UsersListView.as_view(template_name='users/users_list.html'), name='users_list'),
]
