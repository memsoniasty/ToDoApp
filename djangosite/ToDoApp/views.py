from django.shortcuts import render
from django.http import HttpResponse

from .models import ToDoList


def index(request):
    from django.utils import timezone
    response_text = """<h1 align="center">ToDoApp</h1>"""
    todo_lists = ToDoList.objects.all()

    for todo_list in todo_lists:
        response_text += "<br><h3>%s</h3><ul>" % todo_list.name
        for todo_task in todo_list.todotask_set.all():
            response_text += "<li>%s --> %s:%s on %s</li>" % (
                todo_task.todo_text,
                todo_task.date_created.time().hour,
                todo_task.date_created.time().minute,
                todo_task.date_created.date())
        response_text += "</ul>"

    return HttpResponse(response_text)
