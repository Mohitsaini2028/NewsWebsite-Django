from django.db import models

# Create your models here.
class Contact(models.Model):
    PFirstName=models.CharField(max_length=50,)
    PLastName=models.CharField(max_length=50,)
    PAddress=models.CharField(max_length=200,default=" ")
    PEmail=models.CharField(max_length=120,default=" ")
    PCity=models.CharField(max_length=150,default=" ")
    PState=models.CharField(max_length=150,default=" ")

    def __str__(self):
        return self.PFirstName
