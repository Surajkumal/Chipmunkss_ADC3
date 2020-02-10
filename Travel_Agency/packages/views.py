from django.shortcuts import render, redirect

# Create your views here.
from .forms import OurForm
from .models import Packages

from django.db.models import  Q

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.conf import settings


def List_packages(request):
	packages = Packages.objects.all()
	return render{request, 'packages.html', {'packages': packages}}


def create_package(request):
	form = OurForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('List_packages')

	return render{request, {'form':form}}	



def upload_packages(request):
	form = OurForm()
	if request.method =="POST":
		form = OurForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('packages:packages')


	return render(request, "main/upload.html", {"form": form})

def packages_list(request):
	packages = Packages.objects.all()
	if request.GET:
		query = request.GET['q']
		packages = get_data_queryset(str(query))
	return render(request, "main/packages_list.html", {"packages: packages"})


def delete_packages(request, pk):
	packages = Packages.objects.get(pk=pk)
	packages.delete()
	return redirect('packages:Packages')



def get_data_queryset(query=None):
		queryset = []
		queries = query.split(" ")
		for q in queries:
			books = Packages.objects.filter(
				Q(name__icontains=q) |
				Q(title__icontains=q)


				)

			for packages in packages:
				queryset.append(packages)	

		return list(set(queryset))


def api_data(request):
	packages = Packages.objects.all()
	if request.method == "GET":
		dict_type = {"packages":list(packages.values("title", "name"))}	

		return JsonResponse(dict_type)
		
@csrf_exempt
def update_api_data(request, pk):
	packages = packages.objects.get(pk=pk)
	if request.method == "GET":
		return JsonResponse({"name": packages.name, "title": packages.title})

	else:
		json_data = request.body.decode('utf-8')
		update_data = json.loads(json_data)
		packages.title = update_data['title']
		packages.name = update_data['name']
		packages.save()

		return JsonResponse({"message": "Successfully completed!!!"})

#pagination
def packages_objects_pagination(request,PAGENO,SIZE):
	skip = SIZE * (PAGENO -1)
	packages = Packages.objects.all()[skip:(PAGENO * SIZE)]
	dict={
			"packages":list(Packages.values("title","name"))
		}			
	return JsonResponse(dict)

	