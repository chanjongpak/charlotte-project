from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('events/create/', views.EventCreate.as_view(), name='add_event'),
<<<<<<< HEAD
   
=======
    path('events/saved/', views.saved_events, name = 'saved_events'),
    path('events/<int:event_id>/', views.event_detail, name="detail"),
>>>>>>> be376e728111e8335f9db64d09f4ac4ccc1b9421
]