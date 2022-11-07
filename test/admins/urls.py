import imp
from django.conf.urls import url, path
from . import views

urlpatterns = [
    path('', views.index),
    
]
