from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('subject', 'text_area', 'visibility_status', 'case_status',)