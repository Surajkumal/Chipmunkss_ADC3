from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name= "CABS"

urlpatterns = [
    
    
    path('CABS/',views.Cabs, name='CABS'),
	path('cab/upload/', views.upload_file, name="upload"),
	path('cab/', views.list_file, name='list'),
	path('cab/delete/<int:pk>/', views.delete_file, name="delete"),
	path('cab/<int:id>/', views.update_file, name="update"),
    ]