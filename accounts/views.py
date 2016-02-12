from django.shortcuts import render
from django.conf import settings
# Create your views here.
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignupForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, get_backends, authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import send_signup_confirm_email
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
# Create your views here.

@login_required
def profile(request):
    letter_list = request.user.letter_set.all()
    return render(request, 'accounts/profile.html', {'letter_list': letter_list})

def test(request):
    return render(request,'')

def signup(request):
	if request.method == 'POST':

		form = SignupForm(request.POST)
		if form.is_valid():
			#user = form.save(commit=False)
			#user.is_active = False
			#user.save()
			#send_signup_confirm_email(request, user)
			#return redirect(settings.LOGIN_URL)
			user = form.save()
			backend_cls = get_backends()[0].__class__
			backend_path = backend_cls.__module__+'.'+backend_cls.__name__
			user.backend = backend_path
			auth_login(request, user)
			messages.info(request, 'Welcome')
			return redirect(settings.LOGIN_REDIRECT_URL)

	else:

		form = SignupForm()
	return render(request, 'accounts/signup.html', {'form':form, })
    
def signup_confirm(request, uidb64, token):
    User = get_user_model()

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.info(request, 'you have been confirmed, log in . ;)')
        return redirect(settings.LOGIN_URL)
    else:
        messages.error(request, 'oops, looks like that was a bad link. :-(')
        return redirect(settings.LOGIN_URL)

def logout(request):
    auth_logout(request)
    messages.info(request, 'you have been logged out.')
    messages.success(request, 'log out success.')
    messages.warning(request, 'log out warning, ')
    return redirect('/')



