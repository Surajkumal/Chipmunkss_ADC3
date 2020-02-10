from django.db import models

# Create your models here.
class Cabbing(models.Model):
    Pickup = models.CharField(max_length=150)
    Drop = models.CharField(max_length=150)
    File = models.FileField(upload_to="photo/",null=True)

    def __str__(self):
        return self.Pickup

