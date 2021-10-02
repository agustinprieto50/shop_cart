from django.db import models
from django.db.models.base import Model

# Create your models here.
class Product(models.Model):
    _id = models.CharField(max_length=6, default="", primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    distributor = models.ForeignKey('Distributor', on_delete=models.CASCADE)

class Distributor(models.Model):
    _id = models.CharField(max_length=6, default="", primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)

