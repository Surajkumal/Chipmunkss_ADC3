from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.shortcuts import get_object_or_404
#from rest_framework import viewsets
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
#from .models import Flights
#from Flights.serializers import FlightsSerializers
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
#class FlightsList(APIView):

 #   def get(self, request):
      #  Flights1= Flights.objects.all()
      #  serializer=FlightsSerializers(Flights1, many=True)
      #  return Response(serializer.data)

   # def post(self):
      # pass

@login_required
def home(request):
    return render(request, 'Flights/Flights.html')



#class FlightsViewset(viewsets.ModelViewSet):
  #  queryset = User.objects.all()
  #  serializers_class = serializers.FlightsSerailizers

@login_required
def rooms_from(request ):
    From = request.POST["From"]
    to = request.POST["To"]
    Departing = request.POST["Departure_Date"]
    children = request.POST["Children"]
    adults = request.POST["Adults"]
    Returning =request.POST["Returning"]

    flights = Flights(From=From,To=to,Returning=Returning,Departure_Date=Departing,Children=children,Adults=adults)
    flights.save()
    

        
