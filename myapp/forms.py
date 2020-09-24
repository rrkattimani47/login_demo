from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class RegistrationForm(forms.ModelForm):
    password=forms.CharField(max_length=100,required=True,widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','password','email')


class PasswordResetForm(forms.Form):
    password=forms.CharField(max_length=100,required=True,label="New Password :",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=100,required=True,label=" Confirm Password :",widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data=super().clean()
        if cleaned_data.get('password')!=cleaned_data.get('confirm'):
            raise ValidationError("Passwords Not Matched")
        return cleaned_data