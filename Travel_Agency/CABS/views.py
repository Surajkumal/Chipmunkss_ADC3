from django.shortcuts import render, redirect
from .forms import Usercabsbookform
from .models import CAB
def Cabs(request):
    if request.method == 'POST':
        form = Usercabsbookform(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = Usercabsbookform()
    return render(request, 'CABS/cars.html', {'form': form})

def upload_file(request):
	form = OurForm()
	if request.method == "POST":
		form = OurForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('CABS:list')
	return render(request, "CABS/upload.html",
		{"form":form})

def list_file(request):
	query = ""
	context = {}
	if request.GET:
		query = request.GET['q']
	book = get_data_queryset(query)
	context['cabs'] = cab
	return render(request, "CABS/file_list.html", 
		context)

def update_file(request, id=None):
	instance = get_object_or_404(CAB, id=id)
	form = OurForm()
	if request.method == "POST":
		form = OurForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('CABS:list')
	return render(request, "CABS/upload.html", {"form": form}

def delete_file(request,pk=None):
    cab = CAB.objects.get(pk=pk)
    cab.delete()
    return redirect('CABS:list')


