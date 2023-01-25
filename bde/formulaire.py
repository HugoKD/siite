from django import forms
from django.db import models
class ContactForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(widget=forms.Textarea)
    num = models.EmailField()
    couvert = models.BooleanField()
    mess = models.TextField(blank=True)
    vieux = models.BooleanField()

    def __str(self):
        return self.first_name + '' + self.last_name