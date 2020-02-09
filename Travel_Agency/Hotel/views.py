from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Hotel

@login_required
def hotel(request):
    return render(request, 'Hotel/bookyourstay.html')#when hotel is clicked this returns the bookyourstay html

@login_required
def rooms_from(request ):
    #post the data teken from the user and variable created
    destination = request.POST["Destination"]
    check_in = request.POST["Check_in"]
    check_out = request.POST["Check_out"]
    children = request.POST["Children"]
    adults = request.POST["Adults"]
    #variable created for hotel(model)
    hotels = Hotel(Destination=destination,Check_in=check_in,Check_out=check_out,Children=children,Adults=adults)
    hotels.save()#saves information taken from user in database
    return render(request, 'Hotel/payment.html')

def searchhotel(request):
    hotel = Hotel.objects.all()
    if request.GET:
        query =request.GET['q']
        hotel = get_data_queryset(str(query))
    return render(request, "Hotel/bookyourstay.html",{"hotels":hotel})

def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        hotels = Hotel.objects.filter(
            Q(Destination__icontains=q) |
            Q(check_in__icontains=q)
        )
        for hotel in hotels:
            queryset.append(hotel)
        return list(set(queryset))

def payment(request):
    return render(request, 'Hotel/payment.html') 
