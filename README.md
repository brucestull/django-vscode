# Django Tutorial in Visual Studio Code

* Repository for notes and code in 'Django Tutorial in Visual Studio Code'.

## Resources

* [The Tutorial](https://code.visualstudio.com/docs/python/tutorial-django)
* [My repository](https://github.com/brucestull/django-vscode)
* [Sample code](https://github.com/microsoft/python-sample-vscode-django-tutorial)
* [Django Admin Documentation Generator](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/admindocs/)

## New Concepts and Review

### New Concepts

* "Ctrl + Shift + `":
  * Opens the terminal in VS Code.
  * Prompts for choice of python interpreter and opens the terminal, in the available pipenv, in VS Code.
* `a_string.strf()`
  * String format:

    ![a_string.strf()](./images/strf.png)
* `re`
  * Regular expressions:

    ![re](./images/re.png)
* `re.match()`
  * Matches a regular expression to a string:

    ![re.match()](./images/match.png)
* [Create a code snippet](https://code.visualstudio.com/docs/python/tutorial-django#_create-a-code-snippet):
  * Created in:
    * `C:\Users\FlynntKnapp\AppData\Roaming\Code\User\snippets\html.json`
  * Snippets can be created in the workspace directory if desired.

    ```json
    {
      "Django Tutorial: template extending layout.html": {
        "prefix": "djextlayout",
        "body": [
          "{% extends \"hello/layout.html\" %}",
          "",
          "{% block title %}",
          "$0",
          "{% endblock title %}",
          "",
          "{% block content %}",
          "{% endblock content %}"
        ],
        "description": "Boilerplate template that extends layout.html"
      },
    }
    ```

  * The snippet template comment:

    ```json
    {
      // Place your django-vscode workspace snippets here. Each snippet is defined under a snippet name and has a scope, prefix, body and 
      // description. Add comma separated ids of the languages where the snippet is applicable in the scope field. If scope 
      // is left empty or omitted, the snippet gets applied to all languages. The prefix is what is 
      // used to trigger the snippet and the body will be expanded and inserted. Possible variables are: 
      // $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. 
      // Placeholders with the same ids are connected.
      
      // Example:
      // "Print to console": {
      //     "scope": "javascript,typescript",
      //     "prefix": "log",
      //     "body": [
      //         "console.log('$1');",
      //         "$2"
      //     ],
      //     "description": "Log output to console"
      // }
    }
    ```

### Review

* `python -m pip install --upgrade pip`
  * Upgrades pip.

### Links for Big Concepts

* [Prerequisites](https://code.visualstudio.com/docs/python/tutorial-django#_prerequisites)
* [Create a project environment for the Django tutorial](https://code.visualstudio.com/docs/python/tutorial-django#_create-a-project-environment-for-the-django-tutorial)
* [Create and run a minimal Django app](https://code.visualstudio.com/docs/python/tutorial-django#_create-and-run-a-minimal-django-app)
* [Create a debugger launch profile](https://code.visualstudio.com/docs/python/tutorial-django#_create-a-debugger-launch-profile)
* [Explore the debugger](https://code.visualstudio.com/docs/python/tutorial-django#_explore-the-debugger)
* [Go to Definition and Peek Definition commands](https://code.visualstudio.com/docs/python/tutorial-django#_go-to-definition-and-peek-definition-commands)
* [Use a template to render a page](https://code.visualstudio.com/docs/python/tutorial-django#_use-a-template-to-render-a-page)
* [Serve static files](https://code.visualstudio.com/docs/python/tutorial-django#_serve-static-files)
* [Create multiple templates that extend a base template](https://code.visualstudio.com/docs/python/tutorial-django#_create-multiple-templates-that-extend-a-base-template)
* [Work with data, data models, and migrations](https://code.visualstudio.com/docs/python/tutorial-django#_work-with-data-data-models-and-migrations)
* [Use the debugger with page templates](https://code.visualstudio.com/docs/python/tutorial-django#_use-the-debugger-with-page-templates)
* [Optional activities](https://code.visualstudio.com/docs/python/tutorial-django#_optional-activities)
* [Next steps](https://code.visualstudio.com/docs/python/tutorial-django#_next-steps)

## Related Code Snippets

## Related Django Admin Images

## TODO

## Notes

## Directory Structure
