from django import forms
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ('username', 'password','email','phone_number','profile_pic')

class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ("username", "password", "email", "is_superuser", "is_staff", "is_active", "profile_pic", "phone_number",)
# class UserProfileInfoForm(forms.ModelForm):
   
#     class Meta():
#         model = Customer
#         fields = ()
#         widgets = {}


