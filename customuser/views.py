from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from . import forms

class RegistrationView(CreateView):
    template_name = 'register/registration.html'
    # form_class = UserCreationForm
    form_class = forms.CustomUserRegistrations
    success_url = '/users/'


class AuthLogin(LoginView):
    template_name = 'register/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse("users:user_list")


class Userlist(ListView):
    template_name = 'register/user_list.html'
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.all()
