from django.contrib.auth.forms import AuthenticationForm,forms
from .models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(Widget=forms.TextInput(attrs={
        'class' :'form-control py-4',
        'placeholer':'Введите имя'}))

