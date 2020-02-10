from django import forms

from .models import Cabbing

class UploadForm(forms.ModelForm):
	class Meta:
		
		model = Cabbing
		fields = ('Pickup', 'Drop', 'File')