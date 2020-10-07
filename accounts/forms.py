from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm

from accounts.models import CustomUser


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Imię'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nazwisko'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class UserAuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Hasło'}))

    class Meta:
        fields = ['email', 'password']

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Stare hasło'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Nowe hasło'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz nowe hasło'}))

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']

class EditProfileForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']