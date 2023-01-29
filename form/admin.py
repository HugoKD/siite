from django.contrib import admin
from .models import ContactModel


#admin.site.register(ContactModel)

@admin.register(ContactModel)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('Nom', 'Prénom','Horaire', 'Livraison')
    ordering = ('Horaire',)
    search_fields = ('Horaire','Nom','Menu')
    list_filter = ('Menu', 'Horaire')