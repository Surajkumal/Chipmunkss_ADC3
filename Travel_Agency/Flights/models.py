from django.db import models

# Create your models here.


class Flights(models.Model):
    From = models.CharField(max_length=50)
    To = models.CharField(max_length=50)
    Departure_Date = models.DateField()
    Adults = models.PositiveIntegerField()
    Childrens = models.PositiveIntegerField()