import email
from email.policy import default
from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class user_registration_form(UserCreationForm):
    email= forms.EmailField() #default=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
