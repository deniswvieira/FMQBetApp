from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.template import Context
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from forms import MyRegistrationForm, MyUserEditForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from cauth.models import UserProfile
from django.utils.crypto import get_random_string
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		c = {}
		c['login_active'] = True
		c.update(csrf(request))
		return render_to_response('login.html', c)


def invalid_login(request):
	return render_to_response('invalid.html')

def loggedin(request):
	return render(request, 'loggedin.html')

def logout(request):
	if request.user.is_authenticated:
		auth.logout(request)
		return render_to_response('logout.html')
	else:
		return HttpResponseRedirect('/account/login')

def auth_view(request):	
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/account/loggedin')
	else:
		return HttpResponseRedirect('/account/invalid')

def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		args = {}
		args['register_active'] = True
		if request.GET.get('inv'):
			args['invite'] = request.GET.get('inv')

		if request.method == 'POST':
			form = MyRegistrationForm(request.POST)
			args['form'] = form
			if form.is_valid():
				# Pick data
				invite = request.POST.get('invite')
				initial_balance = int(request.POST.get('balance'))

				# Save user with Default properties
				form.save()

				# Pick the user
				user = User.objects.get(username=form.get_username())

				# Custom USER data
				uinfo = UserProfile()
				uinfo.user = user

				# BALANCE
				if initial_balance > 50:
					initial_balance = initial_balance + (initial_balance * 0.10)

				# Check invite
				if invite:
					try:
						host_user = UserProfile.objects.get(invite_id=invite)
					except UserProfile.DoesNotExist:
						host_user = None

					if host_user:
						initial_balance = initial_balance + 10

				# SAVE USER CUSTOM DATA
				uinfo.initial_balance = initial_balance
				uinfo.invite_id = get_random_string(length=30)
				uinfo.save()
				return HttpResponseRedirect('/account/register_success')
			return render_to_response('register.html', args, {'register_active:':True})

		else:
			args['form'] = MyRegistrationForm()
			
			args.update(csrf(request))
			return render_to_response('register.html', args)



def register_success(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		return render_to_response('register_success.html')


def edit(request):
	if request.user.is_authenticated():
		args = {}
		uinfo = UserProfile.objects.get(user_id=request.user.id)
		args['invite'] = uinfo.invite_id
		args['user'] = request.user
		if request.method == "POST":
			form = MyUserEditForm(request.POST)
			args['form'] = form
			if form.is_valid():
				form.save()
				args['user'] = User.objects.get(id=request.user.id)
				args['success'] = True
				args['form'] = MyUserEditForm()
				args.update(csrf(request))
				return render_to_response('edit_profile.html', args)
		return render(request, 'edit_profile.html', args)
	else:
		return HttpResponseRedirect('/')

def password(request):
	if request.user.is_authenticated():
		args = {}
		form = PasswordChangeForm(request.user)
		args['form'] = form
		if request.method == "POST":
			form = PasswordChangeForm(request.user, data=request.POST)
			args['form'] = form
			if form.is_valid():
				form.save()
				update_session_auth_hash(request, form.user)
				args['form'] = PasswordChangeForm(request.user)
				args['success'] = True
				return render(request, 'edit_password.html', args)
		return render(request, 'edit_password.html', args)
	else:
		return HttpResponseRedirect('/')

@login_required
def passw(request):
	return render(request, 'edit_password.html', args)