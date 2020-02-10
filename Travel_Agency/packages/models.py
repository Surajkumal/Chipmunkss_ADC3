from django.db import models


# Create your models here.

		
class Packages(models.Model):
	title = models.CharField(max_length=100)
	name = models.CharField(max_length=50)
	file = models.FileField(upload_to="image/file")
	date = models.DateTimeField("date booked")

	def __self__(self):
		print(self.title)


	