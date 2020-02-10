from django import forms
from django.contrib.auth.forms import OurForm

from django.contrib.auth.models import User

from .models import Packages 

class OurForm(forms.ModelForm):
	email = forms.EmailField(required=True
		)
	class Meta:
		model = Packages
		fields = ('title', 'name', 'file')


	def save(self, commit=True):
			