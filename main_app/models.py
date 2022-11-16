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
class Comment(models.Model):
    text = models.CharField(max_length = 50)

class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Event Date')
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    category = models.CharField(max_length=1, choices=CATEGORIES, default=CATEGORIES[0][0])
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


 