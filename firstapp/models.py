from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=200, null=True)
    country_code = models.CharField(max_length=200, null=True)

class State(models.Model):
    state_name = models.CharField(max_length=200, null=True)
    state_code = models.CharField(max_length=200, null=True)
    country    =models.ForeignKey(Country,on_delete=models.CASCADE,blank=True, null=True)