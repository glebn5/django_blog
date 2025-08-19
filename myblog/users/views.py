from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegisterCustomUserForm

# Create your views here.
class LoginUser(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

class RegisterUser(CreateView):
    form_class = RegisterCustomUserForm
    success_url = reverse_lazy('users:user_login')
    template_name = 'users/register.html'
