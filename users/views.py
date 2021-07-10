import users
from django.views.generic import ListView
from django.contrib.auth.models import User


class UsersListView(ListView):
    model = User
