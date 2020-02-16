from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Cabbing
from .forms import UploadForm
from django.http import HttpResponse

# Create your views here.
def upload(request):
	if request.method == "POST":
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('cabs:display')
	else:
		form = UploadForm()
	return render(request, "uploads/uploads.html",{"form":form})

def display(request):
    cabbing=Cabbing.objects.all()
    return render(request,"uploads/details.html",{"cabbings":cabbing})

def delete(request, pk = None):
	cabbing = Cabbing.objects.get(pk=pk)
	cabbing.delete()
	return redirect('cabs:display')

def update(request, id=None):
	instance = get_object_or_404(Cabbing, id=id)
	form = UploadForm()
	if request.method == "POST":
		form = UploadForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('cabs:display')
	return render(request, "uploads/uploads.html", {"form": form})

