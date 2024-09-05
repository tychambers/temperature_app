from django.db import models

class Test(models.Model):
    one = models.CharField(max_length=150)
    two = models.CharField(max_length=150)
    three = models.CharField(max_length=150)

class Worldcities(models.Model):
    city = models.CharField(max_length=150)
    city_ascii = models.CharField(max_length=150)
    lat = models.FloatField(max_length=150)
    lng = models.FloatField(max_length=150)
    country = models.CharField(max_length=150)
    iso2 = models.CharField(max_length=150)
    iso3 = models.CharField(max_length=150)
    admin_name = models.CharField(max_length=150)
    capital = models.CharField(max_length=150)
    population = models.CharField(max_length=150)

# Create your models here.
