from django.contrib import admin
from django.urls import path, include
from .views import dejeuner, redirection, erreur1,menu


urlpatterns = [
    path('dejeuner/', dejeuner, name="dejeuner"),
    path('redirection/', redirection, name="redirection"),
    path('erreur1/', erreur1, name="erreur1"),
    path('menu/', menu, name="menu"),
]