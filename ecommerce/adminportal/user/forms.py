from email.policy import default
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.forms import widgets
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ('username', 'password','email','phone_number','profile_pic', 'is_superuser', 'is_staff')
        widgets = { 'username': forms.TextInput(attrs={ 'class' : 'form-group', 
                                            'placeholder': "username*", 
                                            'name': 'display_name',
                                           'required': "required",
                                           'data-error': "username is required"}),
        
        'password' : forms.PasswordInput(attrs={'class' : 'form-group',
                                                'placeholder' : "password*", 
                                                'required': "required",
                                                'name': 'password',
                                                'data-error': "password is required"}),
        'email': forms.EmailInput(attrs={'class' : 'form-group',
                                          'placeholder': 'email*',
                                         'name': 'email',
                                         'required': "required",
                                         'data-error': "email is required"}),
}
    


# class UserProfileInfoForm(forms.ModelForm):
   
#     class Meta():
#         model = Customer
#         fields = ()
#         widgets = {}


