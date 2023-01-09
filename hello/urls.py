from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('hello/<str:name>/', views.greet, name='hello-name'),
]
