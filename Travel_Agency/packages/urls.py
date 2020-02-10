
from django.urls import path, include
from .import views
from .views import packages_list,createpackages, upload_packages, delete_packages

app_name = "packages"
urlpatterns = [
   path('', packages_list, name='packages_list'),	
   path('create_packages/<str:pk>/', views.createPackage, name='createpackages'),

   path("packages/upload/", views.upload_packages, name="upload"),
   path("packages/", views.packages_list, name="packages"),
   path("packages/<int:pk>/", views.delete_packages, name="delete_packages"),
   path('api/', views.api_data, name="api_data"),

   path('change/<int:pk>/', views.update_api_data, name="update_api_data"),


]