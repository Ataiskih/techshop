from django import forms
from allauth.account.forms import ChangePasswordForm, \
    PasswordField, SetPasswordField
from allauth.account.adapter import get_adapter


class MyCustomChangePasswordForm(ChangePasswordForm):

    oldpassword = PasswordField(label=("Current Password"))
    password1 = SetPasswordField(label=("New Password"))
    password2 = PasswordField(label=("New Password (again)"))

    def __init__(self, *args, **kwargs):
        super(MyCustomChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['password1'].user = self.user

    def clean_oldpassword(self):
        if not self.user.check_password(self.cleaned_data.get("oldpassword")):
            raise forms.ValidationError(("Please type your current"
                " password."))
        return self.cleaned_data["oldpassword"]

    def save(self):
        get_adapter().set_password(self.user, self.cleaned_data["password1"])
