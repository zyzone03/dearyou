from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.models import User
from letter.models import Member, Letter, Contact
from letter.forms import LetterForm, ContactForm


# Create your views here.Create

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'letter/index.html', {'form': form})
    
preview = DetailView.as_view(model=Letter)

def letter_new(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            letter = form.save(commit=False)
            letter.author = request.user
            letter = form.save()
            return redirect('letter.views.preview', letter.pk)
    else:
        form = LetterForm()
    return render(request, 'letter/letter_new.html', {'form': form})
    
def letter_confirm(request):
    return render(request, 'letter/letter_confirm.html', {})

def mypage(request, pk):
    me = User.objects.get(pk=pk)
    letter_list = me.letter_set.all()
    return render(request, 'letter/mypage.html', {'me': me, 'letter_list': letter_list})