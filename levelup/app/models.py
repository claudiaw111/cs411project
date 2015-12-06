from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField("user_id", default = 'noID', max_length=10)
    user_name = models.CharField("user_name", max_length= 255)
    #password = models.CharField("password", max_length= 20)
    #user_level = models.PositiveIntegerField(default = '00000000')
    user_strength = models.PositiveIntegerField(default = '0')
    user_agility = models.PositiveIntegerField(default='0')
    user_willpower = models.PositiveIntegerField(default='0')
    user_constitution = models.PositiveIntegerField(default='0')
    user_achievement = models.BinaryField(default = '00000000')
    token = models.CharField("oauth_token", default = '00000000', max_length=50)
    token_secret = models.CharField("oauth_token_secret", default = '00000000', max_length=50)
    group = models.CharField("group", default="None", max_length=255)

class Group(models.Model):
    group_name = models.CharField("group_name", max_length= 255, unique=True)
    group_description = models.TextField()
    creator = models.CharField("creator", default='None',max_length=50)
    member_2 = models.CharField("member_2", default='None',max_length=50)
    member_3 = models.CharField("member_3", default='None',max_length=50)

class Challenge(models.Model):
    challenger = models.CharField("challenger", default='None',max_length=50)
    challengee = models.CharField("challengee", default='None',max_length=50)
    gerExp = models.PositiveIntegerField(default=0)
    geeExp = models.PositiveIntegerField(default=0)
    remain = models.PositiveIntegerField(default=7)
