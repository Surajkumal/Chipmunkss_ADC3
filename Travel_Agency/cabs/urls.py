from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views


app_name = "cabs"

urlpatterns = [
    
    #path('/cabs/',views.home, name='Cabs'),
    path('cab/upload/', views.upload, name='files'),
    path('cab/', views.display, name='display'),
    path('cab/delete/<int:pk>/', views.delete, name='delete'),
    path('cab/<int:id>/', views.update, name='update'),
    
]