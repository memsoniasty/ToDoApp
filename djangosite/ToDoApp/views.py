from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import ToDoList


def index(request):
    if not request.user.is_authenticated:
        return HttpResponse("""Please <a href="login">login</a>...""")
    todo_lists = ToDoList.objects.all()

    context = {'todo_lists': todo_lists}
    return render(request, 'ToDoApp/index.html', context)
