from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #to link the individual part of web
    path('',views.home, name='home' ),
    path('register/',views.register, name='register' ),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('profile/',views.profile, name='profile'),

    ]