from django.db import models

# Create your models here.


class CAB(models.Model):
    Pickup = models.CharField(max_length=150)
    Drop = models.CharField(max_length=150)
