from django.shortcuts import render
from .forms import MyForm

def home(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = MyForm()
    return render(request, 'Flights/Flights.html', {'form': form})