from django.urls import path
from django.contrib import admin
#from rest_framework.urlpatterns import format_suffix_patterns
from Flights import views


urlpatterns = [

    path('Flights/',views.home, name='Flights' ),
   # path('Flights/',views.FlightsList.as_view()),

]