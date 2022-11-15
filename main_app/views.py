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

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'

# def contact_view(request):
#     if request.method == 'POST':  
#         form = ContactForm(request.POST) 
#         if form.is_valid():  
#             send_fields(
#                 form.cleaned_data['name'],
#                 form.cleaned_data['date']
#             )
#             return redirect('/success/')
#     else: 
#         form = ContactForm()
#     return render(request, 'event_form.html', {'form': form})    