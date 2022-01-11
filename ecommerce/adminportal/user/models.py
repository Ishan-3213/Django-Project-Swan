from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import  RegexValidator
from generic.models import BaseField
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


# from generic.models import BaseField
# Create your models here.



class Customer(BaseField):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_user")
    email = models.EmailField(max_length=150,unique=True)
    # phone_number = PhoneNumberField(unique=True,null=False, region = 'IN')
    profile_pic = models.ImageField(upload_to = "profile_pic", blank = True)
    phone_regex = RegexValidator(regex=r'^[7-9]{1}\d{9}', message="Phone number must be entered in the format: '999999999'")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, unique=True) 

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=Customer)
def create_auth_token(sender,instance = None, created = False,  **kwargs):
    if created:
        Token.objects.create(user=instance.user)
    
    