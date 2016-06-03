from django.shortcuts import render
from django.utils import timezone
from .models import Task

def tasknote_list(request):
    tasks = Task.objects.filter(due_date__lte=timezone.now()).order_by('due_date')
    return render(request, 'myapp/tasknote_list.html', {'tasks': tasks})