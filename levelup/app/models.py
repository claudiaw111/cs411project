from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    user_id = models.CharField("user_id", default = 'noID', max_length=10)
    user_name = models.CharField("user_name", max_length= 255)
    #password = models.CharField("password", max_length= 20)
    user_level = models.PositiveIntegerField(default = '00000000')
    user_achievement = models.BinaryField(default = '00000000')
    token = models.CharField("oauth_token", default = '00000000', max_length=50)
    token_secret = models.CharField("oauth_token_secret", default = '00000000', max_length=50)

'''
class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['user_id', 'user_name', 'user_level', 'user_acheivement', 'token', 'token_secret']


class CreateUser(models.Model):
    email = models.CharField("email", max_length=50)
    password = models.CharField("password", max_length=255)

class CreateUserForm(ModelForm):
    class Meta:
        model = CreateUser
        fields = ['email', 'password']


class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
'''