from todo.models import Task
from django.shortcuts import render


def home(request):
    task = Task.objects.filter(is_completed = False).order_by('-updated_at')
    completed_task = Task.objects.filter(is_completed = True)
    context= {
        'tasks': task,
        'completed_task': completed_task,
    }
    return render(request,'home.html', context)