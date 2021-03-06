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
9. Use persisted data in the index view method
  + still waiting for the full html template...

====== START PLAYING WITH HTML ======
10. Finally...use html template for the index page
  + create the index.html file in 'templates/ToDoApp' directory
  + templating language here is not Jinja2, but Django's DTL
    - https://docs.djangoproject.com/en/2.0/topics/templates/
  + second render method parameter is relevant to the 'templates' directory
11. Add Bootstrap to the project:
  + ToDoApp/static/ToDoApp/static/bootstrap-3.3.7 directory copied from the official Bootstrap page
  + Modify the index.html page to load staticfiles and use the bootstrap.min.css  as the stylesheet
    - this "link rel" should be moved to the base.html template in the future
  + use the Bootstrap css classes from the library
    - https://getbootstrap.com/docs/3.3/components/#panels
12. Add navigation bar
  + bootstrap.min.js and jquery-1.12.2.min.js scripts in head zone
  + nav element added in body

====== UNIT TESTING ======
13. Add UnitTests with xml-reporting:
  + install xml-reporting package:
    - File/Settings/Project:ToDoApp/Project Interpreter/'Plus icon'/unittest-xml-reporting/ Install Package
  + edit djangosite/settings.py to use the XMLTestRunner
  + create test logic in ToDoApp/tests.py
    - test creates the mock user, builds a request and tries to get the index page status

====== LOGIN ======
14. Add basic login functionality:
  +  create ToDoApp/templates/registration/login.html
    - csrf token is a Cross Site Request Forgery security: https://docs.djangoproject.com/en/2.0/ref/csrf/
  + define login redirection page in djangosite/settings.py
  + provide login and logout url paths in urls.py
  + rename one navbar button in index.html to be the Logout
  + use information if the user is authenticated to generate the proper index response

