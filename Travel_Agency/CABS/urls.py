from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    
    path('CABS/',views.Cabs, name='CABS'),
    ]