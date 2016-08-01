from django import forms
from django.contrib.auth.models import User
from BetApp.models import Bet
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
			'username',
			'email', 
			'password1', 
			'password2'
		)

	def get_username(self):
		username = self.cleaned_data['username']
		return username

	def save(self, commit=True):
		user = super(MyRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

class MyUserEditForm(forms.Form):

	id = forms.IntegerField()
	username = forms.CharField(max_length=30)
	email = forms.EmailField()

	def clean_username(self):
		data = self.cleaned_data['username']
		try:
			uname = User.objects.get(username=data)
			if uname.id == self.cleaned_data['id']:
				pass
			else:
				raise forms.ValidationError("The username already exists.")
		except User.DoesNotExist:
			pass
		return data

	def clean_email(self):
		data = self.cleaned_data['email']
		try:
			uemail = User.objects.get(email=data)
			if uemail.id == self.cleaned_data['id']:
				pass
			else:
				raise forms.ValidationError("The e-mail already exists on database.")
		except User.DoesNotExist:
			pass
		return data

	def save(self, commit=True):
		user = User.objects.get(id=self.cleaned_data['id'])
		user.username = self.cleaned_data['username']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()

		return user
