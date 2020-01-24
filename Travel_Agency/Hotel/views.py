from django.shortcuts import render



from .forms import RoomForm


def Hotel(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
			
            pass  # does nothing, just trigger the validation
    else:
        form = RoomForm()
    return render(request, 'Hotel/bookyourstay.html', {'form': form})