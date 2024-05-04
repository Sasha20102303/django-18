from django.contrib.auth.forms import AuthenticationForm,UserChangeForm,UserCreationForm,forms from.models import User
from .models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(Widget=forms.TextInput(attrs={
        'class' :'form-control py-4',
        'placeholer':'Введите имя'}))
    last_name = forms.CharField(Widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholer': 'Введите фамилию'}))
    email = forms.CharField(Widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholer': 'Введите email'}))
    password1 = forms.CharField(Widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholer': 'Введите пароль'}))
    password2 = forms.CharField(Widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholer': 'Введите пароль'}))


    class Meta:
        model =User
        fields = ['first_name','last_name','username','password1','password2','email']


