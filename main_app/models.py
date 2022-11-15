from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

CATEGORIES = (
    ('B', 'Business Meeting'),
    ('U', 'UXDI'),
    ('S', 'Software Engineer'),
    ('D', 'Designer'),
    ('F', 'Finance'),
    ('R', 'Real Estate'),
    ('I', 'Self-Improvement'),
    ('M', 'Marketing'),
)
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Event Date')
    category = models.CharField(max_length=1, choices=CATEGORIES, default=CATEGORIES[0][0])


