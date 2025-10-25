# tyJourney/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # route for the main page
    path('', views.index, name='index'), 
    # route for the about me page
    path('about/', views.about_me, name='about_me'), 
]