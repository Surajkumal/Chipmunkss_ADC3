from django.db import models




class Hotel(models.Model):
    Destination = models.CharField(max_length=200)
    Check_in = models.DateTimeField()
    Check_out = models.DateTimeField()
    childern = models.PositiveIntegerField(default=0)
    Adults = models.PositiveIntegerField(default=0)


# Create your models here.

