from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from users.forms import CreateUserForm


class ListUsersView(ListView):
    model = User
    template_name='users/users.html'


class CreateUserView(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name='users/create.html'
