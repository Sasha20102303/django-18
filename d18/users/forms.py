from django.contrib.auth.forms import AuthenticationForm,forms
from .models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']