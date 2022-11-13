from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    error_messsage = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_messsage = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_messsage}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')