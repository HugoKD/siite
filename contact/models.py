from django import forms
from django.db import models

class ContactModel(models.Model):
    Prénom = models.CharField(max_length=20)
    Nom= models.CharField(max_length=20)
    Num= models.CharField(max_length=10)
    Livraison= models.CharField(max_length=30)
    Vieux= models.BooleanField()
    Couvert= models.BooleanField()
    Message= models.TextField(max_length=200, blank=True)


    def __str__(self):
        return self.Prénom + ' ' + self.Nom