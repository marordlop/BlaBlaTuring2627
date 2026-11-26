from django.db import models

# Create your models here.
class Vehicle(models.Model):
    description = models.CharField(max_length=100)
    plate = models.CharField(max_length=10, unique=True)
    active = models.BooleanField()