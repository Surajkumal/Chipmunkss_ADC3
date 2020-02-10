from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views


app_name = "cabs"

urlpatterns = [
    path('cab/upload/', views.upload, name="files"),
    path('cab/', views.display, name="display"),
    path('cab/<int:pk>/', views.delete, name="delete"),
]