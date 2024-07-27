from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    confirmPassword = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'contact_no', 'username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirmPassword")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirmPassword', "Passwords do not match.")

        return cleaned_data
    
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data["password"])  # This hashes the password
        if commit:
            user.save()
        return user
