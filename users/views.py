import users
from django.views.generic import ListView
from django.contrib.auth.models import User


class UsersView(ListView):
    model = User
