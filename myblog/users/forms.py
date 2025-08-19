from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RegisterCustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class ChangeCustomUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


    