from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    #to locate the page when correspounding path is searched
    path('hotel/',views.hotel, name='hotel' ),
    path('rooms_from/',views.rooms_from, name='rooms_from' ),
    path('payment/',views.payment, name='payment' ),
    
    ]