from django.shortcuts import render
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from .choices import testvar
from django.shortcuts import redirect


def tasknote_list(request):
    tasks = Task.objects.filter(due_date__lte=timezone.now()).order_by('due_date')
    abcd = testvar
    return render(request, 'myapp/tasknote_list.html', {'tasks': tasks})

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
            task.author = request.user
            task.created_date = timezone.now()
            task.save()
            return redirect('tasknote_list')
    else:
        form = TaskForm()
    return render(request, 'myapp/task_edit.html', {'form': form})