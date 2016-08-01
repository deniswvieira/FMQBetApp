from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Bet(models.Model):
	bet = models.IntegerField()
	choice = models.IntegerField()
	winnings = models.IntegerField()
	user = models.ForeignKey(User)
