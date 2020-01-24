from django import forms
from .models import Hotel


class RoomForm(forms.ModelForm):
	class Meta:

		model = Hotel 
		fields = ['Destination','Check_in','Check_out','Guest']