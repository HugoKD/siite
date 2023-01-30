from django.contrib import admin
from django.urls import path
from .views import contact

urlpatterns = [
    path('nous-contacter/', contact, name='contact'),
]