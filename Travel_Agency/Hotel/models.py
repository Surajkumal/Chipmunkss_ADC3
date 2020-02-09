from django.db import models




class Hotel(models.Model):
    #for table cration with python in sql
    Destination = models.CharField(max_length=200)
    Check_in = models.DateField()
    Check_out = models.DateField()
    children = models.PositiveIntegerField(default=0)
    Adults = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return (self)