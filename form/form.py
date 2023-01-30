from django import forms
from .models import ContactModel
from django.forms import ModelForm
from django.forms import ModelForm, Textarea


class ContactForm(ModelForm):
    class Meta:
        model= ContactModel
        fields="__all__"

    widgets = {


    }

''