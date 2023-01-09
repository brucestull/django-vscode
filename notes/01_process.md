# Process

1. Create virtual environment

1. Install dependencies

1. Start a Django project:
    * `django-admin startproject web_project .`

1. Create the database:
    * `python manage.py migrate`

1. Start the development server:
    * `python manage.py runserver`

1. Open internet browser to server root:
    * <http://localhost:8000/>

1. Verify Django green rocket page.

1. Create a Django app:
    * `django-admin startapp hello`

1. Add a Django function-based view to the app in [`hello/views.py`](../hello/views.py):

    ```python
    from django.http import HttpResponse

    def home(request):
        return HttpResponse('Goodbuy, World! Enjoy the Sails!')
    ```

1. Add [`hello/urls.py`](../hello/urls.py) to contain app URL patterns:

    ```python
    from django.urls import path

    from . import views

    urlpatterns = [
        path('', views.home, name='home'),
    ]
    ```

1. Add a `path()` with the app's route to the project's URL patterns in [`web_project/urls.py`](../web_project/urls.py):
    * Import `include` from `django.urls`.
    * Add `path('', include('hello.urls')),` to the list of URL patterns.

        ```python
        from django.urls import include

        urlpatterns = [
            #...
            path('', include('hello.urls')),
            #...
        ]
        ```

1. Create launch profile:
    * `C:\Users\FlynntKnapp\Programming\django-vscode\.vscode\launch.json`

        ```json
        {
            // Use IntelliSense to learn about possible attributes.
            // Hover to view descriptions of existing attributes.
            // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "Python: Django",
                    "type": "python",
                    "request": "launch",
                    "program": "${workspaceFolder}\\manage.py",
                    "args": [
                        "runserver"
                    ],
                    "django": true,
                    "justMyCode": true
                }
            ]
        }
        ```

1. Open internet browser to server root:
    * <http://localhost:8000/>

1. Add another view which accepts a URL parameter:
    * [`hello/views.py`](../hello/views.py):

        ```python
        def greet(request, name):
            now = datetime.now()
            formatted_now = now.strftime('%A, %d %B, %Y at %X')
            # match_object = re.match(r'^[A-Z][a-z]+$', name) # Copilot
            match_object = re.match("[a-zA-Z]+", name)
            if match_object:
                clean_name = match_object.group(0)
            else:
                clean_name = 'Fiend'
            content = "Greetings, " + clean_name + "! It's " + formatted_now
            return HttpResponse(content)
        ```

1. Open internet browser to app route:
    * <http://localhost:8000/hello/Dezzi/>
    * <http://localhost:8000/hello/Greta/>
    * <http://localhost:8000/hello/ShalerMoon/>
    * <http://localhost:8000/hello/Shaler:Moon/>
    * <http://localhost:8000/hello/Bunbun/>
