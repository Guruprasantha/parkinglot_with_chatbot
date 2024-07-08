
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Login(models.Model):
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=100)


class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phonenumber = models.IntegerField(null=True)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    oname=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    car=models.CharField(max_length=50)
    carnumber=models.CharField(max_length=50)
    intime = models.TimeField(null=True)
    outtime = models.TimeField(null=True)
    indate=models.CharField(max_length=20)
    outdate=models.CharField(max_length=20)

    def __str___(self):
        return self.oname


    
    