from django.db import models


class ToDoList(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField('date created')


class ToDoTask(models.Model):
    todo_text = models.CharField(max_length=300)
    date_created = models.DateTimeField('date created')
    is_todo = models.BooleanField(default=False)
    is_inprogress = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    date_finished = models.DateTimeField(default=None, null=True, verbose_name='date finished')

    list_ref = models.ForeignKey(ToDoList, on_delete=models.DO_NOTHING)

