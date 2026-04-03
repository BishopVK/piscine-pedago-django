# 1. Check Django it's installed and verify version
```bash
python -m django --version
```

# 2. Create Django project
Create project folder
```bash
mkdir django_project
```

create Django project
```bash
django-admin startproject mysite django_project
```

# 3. Run developer server
Create project folder
```bash
cd django_project
python manage.py runserver
```

If all it's correct, you could open http://127.0.0.1:8000/ in your browser

# 4. Create application
Inside the project forder *(django_project)*, at manane.py level we will create app directory **hello_world**
```bash
python manage.py startapp hello_world
cd hello_world
```

# 5. Our first view
To create our first view, we must enter on our app folder *(hello_world)*, and add into views.py:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the hello_world index.")
```

# 6. Defining URL conf
We need to create **urls.py** file inside app folder
```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

# 7 Configure URL conf in the *mysite* folder
Go up to hello_world root folder:
```bash
cd ..
```

Add **include** package to the **django.urls** import line:
```bash
# add include to imports
from django.urls import include, path
```

Add **hello_world** to *urlpatterns* list whit the **helloworld** path:
```bash
urlpatterns = [
    # Adding hello_world to the urls path
    path("helloworld/", include("hello_world.urls")),
    path('admin/', admin.site.urls),
]
```

# 8. Launch server
If the server it's down, you can launch it again:
```bash
python manage.py runserver
```

# 9. Your app view!
You can see the result of your work visiting http://127.0.0.1:8000/helloworld