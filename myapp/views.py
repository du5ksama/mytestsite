from django.shortcuts import render
from django.utils import timezone
from .models import *
from .forms import *
from .choices import *
from django.shortcuts import redirect
from django.contrib.auth.models import User

def tasknote_list(request):
    tasks = Task.objects.order_by('due_date')
    notes = Note.objects.filter(created_date__lte=timezone.now())
    return render(request, 'myapp/tasknote_list.html', {
                                                        'tasks': tasks,
                                                        'notes': notes,
                                                        'VISIBILITY_CHOICES': VISIBILITY_CHOICES,
                                                        'CASE_CHOICES': CASE_CHOICES,
                                                        'testvar1': testvar1
                                                        })

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task()
            task.subject = form.cleaned_data['subject']
            task.text_area = form.cleaned_data['text_area']
            task.visibility_status = form.cleaned_data['visibility_status']
            task.case_status = form.cleaned_data['case_status']
            task.due_date = form.cleaned_data['due_date']
            task.assigned_to = form.cleaned_data['assigned_to']
            task.author = User.objects.get(id=1)
            #task.author = request.user
            task.created_date = timezone.now()
            task.save()
            return redirect('tasknote_list')
    else:
        form = TaskForm()
    return render(request, 'myapp/task_edit.html', {'form': form})

def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            return redirect('tasknote_list')
    else:
        form = NoteForm()
    return render(request, 'myapp/note_edit.html', {'form': form})