from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.contrib.auth.models import User
from .choices import *

from .models import *

class TaskForm(forms.Form):
    subject = forms.CharField(max_length=200)
    assigned_to = forms.ModelChoiceField(queryset=User.objects.all())
    text_area = forms.CharField(widget=forms.Textarea)
    visibility_status = forms.ChoiceField(choices=VISIBILITY_CHOICES,)
    case_status = forms.ChoiceField(choices=CASE_CHOICES,)
    due_date = forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD","pickTime": False}))

    #class Meta:
    #    model = Task
    #    fields = ('subject', 'text_area', 'visibility_status', 'case_status','due_date',)
    
class NoteForm(forms.Form):
    subject = forms.CharField(max_length=200)
    assigned_to = forms.ModelChoiceField(queryset=User.objects.all())
    text_area = forms.CharField(widget=forms.Textarea)
    visibility_status = forms.ChoiceField(choices=VISIBILITY_CHOICES,)