from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.core import serializers
#Decorator to use built-in authentication system
from django.contrib.auth.decorators import login_required

#Used to create and manually log in a user
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

#forms
from whatsgoingon.forms import *
from django.contrib.auth.forms import UserCreationForm

#Used to get time
import datetime

#for requeset
from django.http import HttpResponse, Http404

#for pictures
from mimetypes import guess_type

#for mails
from django.core.mail import send_mail

#for token email registration
from django.contrib.auth.tokens import default_token_generator

from whatsgoingon.models import *

from .tokens import account_activation_token



def main(request):
	return 
