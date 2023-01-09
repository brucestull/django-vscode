from django.urls import path

from . import views


app_name = 'hello'
urlpatterns = [
    path('', views.home, name='home'),
    path('ext/<str:name>/', views.hello_there_extended, name='hello_there_extended'),
    path('<str:name>/', views.hello_there, name='hello_there'),
]