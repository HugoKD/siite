from django.contrib import admin
from .models import ContactModel,PlaceDispo



@admin.register(ContactModel)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('Nom', 'Prenom','Horaire', 'Adresse')
    ordering = ('Horaire',)
    search_fields = ('Horaire','Nom','Menu')
    list_filter = ('Menu', 'Horaire')


@admin.register(PlaceDispo)

class PlaceDispoAdmin(admin.ModelAdmin):
    list_display = ('Count','Horaire')
    ordering = ('Count',)


