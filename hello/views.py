import re

from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.views.generic import ListView

from .forms import LogMessageForm
from .models import LogMessage


# def home(request):
#     return HttpResponse('Goodbuy, World! Enjoy the sails!')


# def home(request):
#     return render(request, 'hello/home.html')


class HomeListView(ListView):
    """
    Renders the home page, with a list of `LogMessage`s.
    """
    model = LogMessage

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        context = super(HomeListView, self).get_context_data(**kwargs)

        # Probably don't need this since we're using a `ListView` which uses the `model` attribute to determine the form.
        # context['form'] = LogMessageForm()
        
        return context


def about(request):
    return render(request, 'hello/about.html')


def contact(request):
    return render(request, 'hello/contact.html')


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            log_message = form.save(commit=False)
            log_message.log_date = datetime.now()
            log_message.save()
            return redirect('home')

    else:
        return render(request, 'hello/log_message.html', {'form': form})


def hello_there_extended(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)


def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )