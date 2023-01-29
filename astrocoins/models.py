from django.db import models
from django.contrib import admin

class Classement(models.Model):
    prenom = models.CharField(max_length=25)
    nom = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)
    points = models.IntegerField()
    rang = models.IntegerField(default=0)


class ClassementAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'points')
    list_filter = ('points',)
    search_fields = ['prenom', 'nom']