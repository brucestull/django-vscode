from django.urls import path

from . import views
from . import models


home_list_view = views.HomeListView.as_view(
    queryset=models.LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="log_message_list",
    template_name="hello/home.html",
)


urlpatterns = [
    # path('', views.home, name='home'),
    path('', home_list_view, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('log/', views.log_message, name='log'),

    path('ext/<str:name>/', views.hello_there_extended, name='hello_there_extended'),
    path('<str:name>/', views.hello_there, name='hello_there'),
]