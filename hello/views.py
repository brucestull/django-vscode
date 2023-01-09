import re

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime


def home(request):
    return HttpResponse('Goodbuy, World! Enjoy the Sails!')


def greet(request, name):
    """
    View function to greet a user by name provided in the URL.
    """
    return render(
        request,
        "hello/greet.html",
        {
            'name': name,
            'date': datetime.now()
        }
    )

# def greet(request, name):
#     """
#     View function to greet a user by name provided in the URL.
#     """
#     now = datetime.now()
#     formatted_now = now.strftime('%a, %d %b, %Y at %X')
#     # match_object = re.match(r'^[A-Z][a-z]+$', name) # Copilot
#     match_object = re.match("[a-zA-Z]+", name)
#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = 'Fiend'
#     content = (
#         "Greetings, " +
#         clean_name +
#         "! It's " +
#         formatted_now
#     )
#     return HttpResponse(content)

