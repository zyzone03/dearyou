from django.shortcuts import render, redirect
from letter.models import Member, Letter
from letter.forms import LetterForm
from django.contrib.auth.models import User

# Create your views here.Create

def index(request):
    return render(request, 'letter/index.html')
    
def letter_new(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            letter = form.save()
            return redirect('/')
    else:
        form = LetterForm()
    return render(request, 'letter/letter_new.html', {'form': form})

def mypage(request, pk):
    me = User.objects.get(pk=pk)
    letter_list = me.letter_set.all()
    return render(request, 'letter/mypage.html', {'me': me, 'letter_list': letter_list})