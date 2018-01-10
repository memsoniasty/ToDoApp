====== CONFIGURE PYTHON AND DJANGO ======
1. Set the virtualenv python interpreter to inherit from python 3.5.2
  + File/Settings/Project:ToDOApp/ProjectInterpreter// GearWheel Icon -> Create VirtualEnv
2. Add Django to the packages list, then hit Install Package
  + after this process is complete, go to Terminal in PyCharm and type: django-admin --version

====== START THE PROJECT ======
3. django-admin startproject djangosite - to create the site layout
4. python manage.py migrate - to migrate models into db.sqlite3 database schema