from django import forms
from .models import Packages 

class OurForm(forms.ModelForm):
	class Meta:
		model = Packages
		fields = ('title', 'name', 'file')