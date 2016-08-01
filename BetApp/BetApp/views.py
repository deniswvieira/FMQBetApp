from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from cauth.models import UserProfile
from BetApp.models import Bet
from forms import BetForm
from random import randint
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	if request.user.is_authenticated():
		return render(request, 'index.html', {'home_active': True})
	else:
		return render(request, 'index.html', {'home_active': True})

def balance(request):
	if request.user.is_authenticated():
		profile = UserProfile.objects.get(user_id=request.user.id)
		if request.method == "POST":
			input_balance = int(request.POST.get('balance'))
			if input_balance > 50:
				input_balance += input_balance * 0.10
			profile.initial_balance += input_balance
			profile.save()
		balance = int(profile.initial_balance)
		return render(request, 'balance.html', {'balance': balance, 'balance_active': True})
	else:
		return HttpResponseRedirect('/')


def bet(request):
	if request.user.is_authenticated():
		profile = UserProfile.objects.get(user_id=request.user.id)
		balance = int(profile.initial_balance)
		if request.method == "POST":
			form = BetForm(request.POST)
			if form.is_valid:
				bet = int(request.POST.get('bet'))
				choice = 1
				if bet > balance:
					return render(request, 'bet.html', {'bet_active': True, 'balance': balance, 'errors': True, 'error': 'You do not have suficient credits.'})
				elif bet == 0 or bet > 20:
					return render(request, 'bet.html', {'bet_active': True, 'balance': balance, 'errors': True, 'error': 'You must bet 1 - 20.'})
				else:
					# --------- bet logic
					# 0 -> win  1 -> lose
					choice = randint(0,1)
					win = bet + (20/bet) * 100
					betDB = Bet()
					betDB.bet = bet
					betDB.choice = choice
					betDB.winnings = win
					betDB.user = request.user
					betDB.save()

					# Update user balance
					profile.initial_balance -= bet

					if choice == 0:
						profile.initial_balance += win
						profile.save()
						balance = int(profile.initial_balance)
						return render(request, 'bet.html', {'bet_active': True, 'balance': balance, 'play': True, 'win': win, 'winner': True})
					else:
						profile.save()
						balance = int(profile.initial_balance)
						return render(request, 'bet.html', {'bet_active': True, 'balance': balance, 'play': True, 'win': 0, 'winner': False})
		else:
			return render(request, 'bet.html', {'bet_active': True, 'balance': balance, 'play': False})
	else:
		return HttpResponseRedirect('/')