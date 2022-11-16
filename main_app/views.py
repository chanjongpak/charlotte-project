from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import CommentForm
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

def add_comment(request, event_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.event_id = event_id
        new_comment.save()
    return redirect('detail', event_id = event_id)

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'date', 'location', 'address', 'category']
    success_url = '/events/saved/'

class EventUpdate(UpdateView):
    model = Event
    fields = ['name', 'date', 'location', 'address', 'category']
    success_url = '/events/saved/'

class EventDelete(DeleteView):
    model = Event
    success_url = '/events/saved/'