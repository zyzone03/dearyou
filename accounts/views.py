from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignupForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, get_backends, authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def profile(request, pk):
    user = User.objects.get(pk=pk)
    letter_list = user.letter_set.all()
    return render(request, 'accounts/profile.html', {'user': user, 'letter_list': letter_list})

def test(request):
    return render(request,'')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
#        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            #return render(request, 'accounts/profile.html')
            #return render(request, 'accounts/login.html')
            #return render(request, '/index.html')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html' , {'form': form,
    })

def logout(request):
    auth_logout(request)
    return redirect('/')



