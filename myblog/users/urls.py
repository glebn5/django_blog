from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('user_login/', LoginUser.as_view(), name='user_login'),
    path('user_logout/', LoginView.as_view(), name = 'user_logout'),
    path('user_reg/', RegisterUser.as_view(), name = 'user_register')
]