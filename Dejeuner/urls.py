from django.contrib import admin
from django.urls import path, include
from .views import dejeuner, redirection


urlpatterns = [
    path('dejeuner/', dejeuner, name="dejeuner"),
    path('redirection/', redirection, name="redirection"),

]