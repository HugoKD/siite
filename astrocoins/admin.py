from django.contrib import admin
from .models import Classement, ClassementAdmin

admin.site.register(Classement, ClassementAdmin)
