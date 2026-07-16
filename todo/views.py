from django.http import HttpResponse
from django.shortcuts import render

from todo.models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create()
    return HttpResponse('the form is submited')  