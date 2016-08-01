from django import forms
from django.contrib.auth.models import User
from BetApp.models import Bet
from django.contrib.auth.forms import UserCreationForm


class BetForm(forms.ModelForm):
	bet = forms.IntegerField()

	class Meta:
		model = Bet
		fields = {'bet'}

