from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = User
        Fieds =['username' ,'Email' ,'Password' ,'Confirm_Password']