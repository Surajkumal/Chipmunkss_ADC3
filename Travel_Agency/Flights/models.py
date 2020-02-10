from django.db import models

# Create your models here.

#fileds where data is insserted in forms

#objects = models.Manager()

class Flights(models.Model):
    From=models.CharField(max_length=50)
    To=models.CharField(max_length=50)
    Departure_Date=models.DateField()
    Adults=models.PositiveIntegerField(default=0)
    Childrens=models.PositiveIntegerField(default=0)

    #def __str__(self):
      # return self.Departure_Date


# Create / Insert / Add - POST
# Retriveve / Fetch - GET
# Update / Edit - PUT 
# Delete / Remove - DELETE  