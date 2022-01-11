from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.forms import widgets
from .models import Customer


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    

    class Meta():
        model = User
        fields = ('username', 'password')
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
}
    


class UserProfileInfoForm(forms.ModelForm):
   
    class Meta():
        model = Customer
        fields = ('phone_number','profile_pic','email')
        widgets = {'email': forms.EmailInput(attrs={'class' : 'form-group',
                                          'placeholder': 'email*',
                                         'name': 'email',
                                         'required': "required",
                                         'data-error': "email is required"}),}


