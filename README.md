====== CONFIGURE PYTHON AND DJANGO ======
1. Set the virtualenv python interpreter to inherit from python 3.5.2
  + File/Settings/Project:ToDOApp/ProjectInterpreter// GearWheel Icon -> Create VirtualEnv
2. Add Django to the packages list, then hit Install Package
  + after this process is complete, go to Terminal in PyCharm and type: django-admin --version

====== START THE PROJECT ======
3. django-admin startproject djangosite - to create the site layout
4. python manage.py migrate - to migrate models into db.sqlite3 database schema
5.python manage.py createsuperuser - to...surprise - create the superuser :)
6. python manage.py startapp ToDoApp - to create the application layout

====== CREATE SOME LOGIC ======
7. Create the index page logic:
  + create ToDoApp/urls.py with the application relative paths
    - the views.index is the method reference in ToDoApp/views.py
  + include ToDoApp/urls.py in djangosite/urls.py - to keep applictaion paths separated
  + implement index method in ToDoApp/views.py
    - this method will use its own html file in the future
8. Create persistence models:
  + djangosite/settings.py - add ToDoApp to the installed apps list
  + visit models.py - to provide classes definitions for the persistence layer
  + python manage.py makemigrations ToDoApp - to create the db schema for the models
    - visit ToDoApp/migrations directory to see what happened
8.1. python manage.py shell - to play with persisted data:
  + modify date_finished field in ToDoApp/models.py
    default=None does not allow or disallow a None value to be used.
    It simply tells Django what should be the value of the field if it is not specified.
    null=True does allow None to be used in the Python code
  + >> import django
    >>> django.setup()
    >>> from ToDoApp.models import ToDoList, ToDoTask
    >>> ToDoList.objects.all()
    <QuerySet []>
    >>> from django.utils import timezone
    >>> l = ToDoList(name="TestToDoList", date_created=timezone.now())
    >>> l
    <ToDoList: ToDoList object (None)>
    >>> l.save()
    >>> ToDoList.objects.all()
    <QuerySet [<ToDoList: ToDoList object (1)>]>
    >>> ToDoList.objects.get(name="TestToDoList").pk
    1
    >>> ToDoList.objects.get(name="TestToDoList").date_created
    datetime.datetime(2018, 1, 10, 15, 9, 17, 455284, tzinfo=<UTC>)
    >>> tz = timezone.now()
    l.todotask_set.create(todo_text="Keep it up!", date_created=tz)
    <ToDoTask: ToDoTask object (1)>
    >>>
  + add appropriate code to ToDoApp/admin.py - to register the models on the admin page
    - go to <server_ip>:<port>/admin - to see all your data

