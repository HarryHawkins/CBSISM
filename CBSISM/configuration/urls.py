from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

#from . import add_endpoint
urlpatterns = [
   path('', views.add_endpoint,name='Add Endpoint'),
   path('remove', views.remove_endpoint,name='Remove Endpoint'),

   ]
