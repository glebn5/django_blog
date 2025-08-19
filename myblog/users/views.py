from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
class LoginUser(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

