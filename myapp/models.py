from django.db import models
from django.utils import timezone


class Task(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    subject = models.CharField(max_length=200)
    text_area = models.TextField()
    visibility_status = models.IntegerField()
    author = models.ForeignKey('auth.User')
    
    case_status = models.IntegerField()
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