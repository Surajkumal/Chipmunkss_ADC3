from django.shortcuts import render



from .models import Hotel




def hotel(request):
    return render(request, 'Hotel/bookyourstay.html')

def rooms_from(request ):
    destination = request.POST["Destination"]
    check_in = request.POST["Check_in"]
    check_out = request.POST["Check_out"]
    children = request.POST["Children"]
    adults = request.POST["Adults"]

    hotels = Hotel(Destination=destination,Check_in=check_in,Check_out=check_out,Children=children,Adults=adults)
    hotels.save()
    return render(request, 'Hotel/payment.html')