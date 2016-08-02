from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	initial_balance = models.IntegerField()
	invite_id = models.CharField(max_length=30)
	