from django.urls import path
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    path('temp/', TemplateView.as_view(template_name='hello/temp.html'), name='temp'),

    path('', views.home, name='home'),
    path('hello/<str:name>/', views.greet, name='greet'),
]
