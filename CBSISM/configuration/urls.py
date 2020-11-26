from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import add_endpoint
urlpatterns = [
   path('add_endpoint/', add_endpoint.add_endpoint)]
