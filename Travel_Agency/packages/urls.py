
from django.urls import path, include
from .import views

app_name = "packages"
urlpatterns = [
   path('', List_packages, name='List_packages'),
   path("packages/upload/", views.upload_packages, name="upload"),
   path("packages/", views.packages_list, name="packages"),
   path("packages/<int:pk>/", views.delete_packages, name="delete_packages"),
   path('api/', views.api_data, name="api_data"),

   path('change/<int:pk>/', views.update_api_data, name="update_api_data"),
]