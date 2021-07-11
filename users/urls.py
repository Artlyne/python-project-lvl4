from django.urls import path
from users.views import UsersView

urlpatterns = [
    path('', UsersView.as_view(template_name='users/users.html'), name='users'),
]
