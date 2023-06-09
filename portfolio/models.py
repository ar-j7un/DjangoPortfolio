from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name=models.CharField(max_length=100)
    college1=models.CharField(max_length=100)
    college2=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    phone=models.IntegerField()
    place=models.CharField(max_length=100)