from django.contrib import admin
from .models import ContactModel,PlaceDispo, CompteurMenu



@admin.register(ContactModel)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('Nom', 'Prenom','Horaire', 'Adresse', 'Menu','Boisson', 'Vieux', 'Message')
    ordering = ('Horaire',)
    search_fields = ('Horaire','Nom','Menu')
    list_filter = ('Menu', 'Horaire')


@admin.register(PlaceDispo)

class PlaceDispoAdmin(admin.ModelAdmin):
    list_display = ('Count','Horaire')
    ordering = ('Count',)

@admin.register(CompteurMenu)

class CompteurMenuAdmin(admin.ModelAdmin):
    list_display = ('menu','compteur')
    ordering = ('compteur',)
