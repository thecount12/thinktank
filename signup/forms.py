
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    hint = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'hint', 'password1', 'password2',)
