from todo.models import Task
from django.shortcuts import render


def home(request):
    task = Task.objects.filter(is_completed = False)
    context= {
        'tasks': task,
    }
    return render(request,'home.html', context)