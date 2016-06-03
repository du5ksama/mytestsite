from django.shortcuts import render

def tasknote_list(request):
    return render(request, 'myapp/tasknote_list.html', {})