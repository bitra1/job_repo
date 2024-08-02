from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=30)

class VijJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=30)

class BangJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=30)
        
