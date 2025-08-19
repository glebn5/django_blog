from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterCustomUserForm, ChangeCustomUserForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = RegisterCustomUserForm
    form = ChangeCustomUserForm
    model = CustomUser
    list_display = ['username', 'email']
    list_display_links = ['username']
    list_filter = ['username']

admin.site.register(CustomUser, CustomUserAdmin)

