from django import forms
from .models import ContactModel
from django.forms import ModelForm


class ContactForm(ModelForm):
    class Meta:
        model= ContactModel
        fields="__all__"

''