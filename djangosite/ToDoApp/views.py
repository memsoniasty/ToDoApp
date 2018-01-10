from django.shortcuts import render
from django.http import HttpResponse

from .models import ToDoList


def index(request):
    todo_lists = ToDoList.objects.all()

    context = {'todo_lists': todo_lists}
    return render(request, 'ToDoApp/index.html', context)
