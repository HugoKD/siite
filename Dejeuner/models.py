from django import forms
from django.db import models


class PlaceDispo(models.Model):
    Horaire=models.CharField(max_length=5)
    Count=models.IntegerField(default=25)


class ContactModel(models.Model):
    Prenom = models.CharField(max_length=20)
    Nom= models.CharField(max_length=20)
    Num= models.CharField(max_length=10)
    Adresse= models.CharField(max_length=30)
    Vieux= models.BooleanField()
    Couvert = models.BooleanField()
    Horaire= models.CharField(max_length=10)
    Menu = models.CharField(max_length=10)
    Message= models.TextField(max_length=200, blank=True)
    Boisson= models.CharField(max_length=20)



    def __str__(self):
        return self.Prenom + ' ' + self.Nom