from allauth.account.forms import ChangePasswordForm, \
    AddEmailForm, PasswordField, SetPasswordField
from django import forms
from django.contrib.auth.models import User


class MyCustomChangePasswordForm(ChangePasswordForm, forms.ModelForm):

    oldpassword = PasswordField(label= ("Current Password"))
    password1 = SetPasswordField(label= ("New Password"))
    password2 = PasswordField(label= ("New Password (again)"))

    class Meta:
        model = User
        fields = ["oldpassword", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['password1'].user = self.user

    def clean_oldpassword(self):
        if not self.user.check_password(self.cleaned_data.get("oldpassword")):
            raise forms.ValidationError(_("Please type your current"
                                          " password."))
        return self.cleaned_data["oldpassword"]

    def save(self):
        get_adapter().set_password(self.user, self.cleaned_data["password1"])


class ChangePersonalInfo(forms.ModelForm):

    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]

