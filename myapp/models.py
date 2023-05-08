from django.db import models

class Feature(models.Model):
    name= models.CharField(max_length=100)
    det= models.CharField(max_length=500)
    
# Create your models here.
