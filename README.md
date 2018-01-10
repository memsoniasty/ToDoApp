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

