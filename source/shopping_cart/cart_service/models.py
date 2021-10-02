from django.db import models
from django.db.models.base import Model
from django.db.models.fields import FloatField

# holis 
# Create your models here.
class Users(models.Model):
    _id = models.IntegerField(max_length=6, default="", primary_key=True)
    #name = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_lenght=50)
    email = models.EmailField(max_lenght=50)
    password = models.CharField(max_length=20)
    type = models.BooleanField()

class Clients(models.Model):
    _id = models.IntegerField(max_length=6, default="", primary_key=True)
    address = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=12)


class PurchasedProducts(models.Model): 
    _id = models.IntegerField(max_length=6, default="", primary_key=True)
    name = models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    idOriginalProduct = models.ForeignKey()
    salePrice = models.FloatField(max_length=50)
    amount = models.IntegerField(max_length=12)

class Sales(models.Model):
    _id = models.IntegerField(max_length=6, default="", primary_key=True)
    user = models.CharField(max_length=50)
    productList = models.IntegerField(max_length=20)
    saleDate = models.DateField()

class ProductList(models.Model):
    _id = models.IntegerField(max_length=6, default="", primary_key=True)
    idOrginalProduct = models.ForeignKey()
    amount = models.IntegerField(max_length=12)


class ShoppingCarts(models.Model): 
    _id = models.IntegerField(max_length=6, default="", primary_key=True)