#from django.shortcuts import render

# Create your views here.
#def Cabs(request):
 #   return render(request,'CABS/cars.html')


from django.shortcuts import render
from .forms import Usercabsbookform

def Cabs(request):
    if request.method == 'POST':
        form = Usercabsbookform(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = Usercabsbookform()
    return render(request, 'CABS/cars.html', {'form': form})