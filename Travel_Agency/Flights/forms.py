from django import forms
from .models import Flights


class MyForm(forms.ModelForm):
	class Meta:

		model = Flights 
		fields = ['From','To','Departure_Date','Adults','Childrens']