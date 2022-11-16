from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/saved/', views.saved_events, name = 'saved_events'),
    path('events/<int:event_id>/', views.event_detail, name="detail"),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name="events_update"),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name="events_delete"),
]
