from django.contrib import admin
from django.urls import path
from .views import contact,redirection

urlpatterns = [
    path('nous-contacter/', contact, name='contact'),
    path('redirection/',redirection,name='redirection')
]