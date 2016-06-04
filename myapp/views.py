from django.shortcuts import render
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect

def tasknote_list(request):
    tasks = Task.objects.filter(due_date__lte=timezone.now()).order_by('due_date')
    return render(request, 'myapp/tasknote_list.html', {'tasks': tasks})

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.created_date = timezone.now()
            task.save()
            return redirect('tasknote_list')
    else:
        form = TaskForm()
    return render(request, 'myapp/task_edit.html', {'form': form})