from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Event
from django.http import HttpResponseRedirect 

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

def saved_events(request):
    events = Event.objects.all()
    return render(request, 'saved_events.html', { 'events': events })

def event_detail(request, event_id):
    event = Event.objects.get(id = event_id)
    return render(request, 'events/detail.html', { 'event': event })


class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'

def contact_view(request):
    if request.method == 'POST':  
        form = NewContactForm() 
        if form.is_valid():  
            form.save()
            return redirect('/detail_form')
    else: 
        form = NewContactForm()
    return render(request, 'event_form.html', {'form': form}) 

# cj daddy take a look at this   