from allauth.account.forms import ChangePasswordForm, AddEmailForm
from django import forms
from django.contrib.auth.models import User

class MyCustomChangePasswordForm(ChangePasswordForm):
    oldpassword = ChangePasswordForm()
    password1 = ChangePasswordForm()
    password2 = ChangePasswordForm()

class ChangePersonalInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


