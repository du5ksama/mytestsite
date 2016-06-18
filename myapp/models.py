from django.db import models
from django.utils import timezone
from .choices import *
from django.contrib.auth.models import User

class Task(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    subject = models.CharField(max_length=200)
    text_area = models.TextField()
    visibility_status = models.IntegerField(choices=VISIBILITY_CHOICES)
    author = models.ForeignKey('auth.User')
    assigned_to = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name='+')
    
    case_status = models.IntegerField(choices=CASE_CHOICES)
    due_date = models.DateField(blank=True, null=True)

    def save_task(self):
        self.due_date = timezone.now()
        self.save()

    def __str__(self):
        return self.subject
    
class Note(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    subject = models.CharField(max_length=200)
    text_area = models.TextField()
    visibility_status = models.IntegerField()
    author = models.ForeignKey('auth.User')

    def save_note(self):
        self.due_date = timezone.now()
        self.save()

    def __str__(self):
        return self.subject