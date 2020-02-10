from django import forms
from .models import CAB


class Usercabsbookform(forms.ModelForm):
	class Meta:

		model = CAB
		fields = ['Pickup','Drop']