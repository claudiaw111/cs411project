from django.db import models
from django.forms import ModelForm
# Create your models here.

class Users(models.Model):
    user_name = models.CharField("user", max_length= 255)
    password = models.CharField("password", max_length= 20)

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['user_name', 'password']