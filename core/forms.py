from allauth.account.forms import ChangePasswordForm, \
    AddEmailForm, PasswordField, SetPasswordField
from django import forms
from django.contrib.auth.models import User


class MyCustomChangePasswordForm(ChangePasswordForm):
    oldpassword = PasswordField()
    password1 = SetPasswordField()
    password2 = PasswordField()

class ChangePersonalInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


