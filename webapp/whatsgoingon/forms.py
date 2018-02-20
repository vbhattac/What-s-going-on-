from django import forms
from django.contrib.auth.forms import UserCreationForm
from whatsgoingon.models import *

class LoginForm(forms.Form):
	username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username'}))
	password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))



class RegisterForm(UserCreationForm):
	email = forms.EmailField(label='Email')
	firstname = forms.CharField(label='Firstname')
	lastname = forms.CharField(label='Lastname')


class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude =('orgnizer',)
		widgets = {'photo':forms.FileInput()}

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile 
		exclude = ('owner', 'friendlist',)
		widgets = {'photo':forms.FileInput()}
