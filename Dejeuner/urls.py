from django.contrib import admin
from django.urls import path,include
from .views import dejeuner

urlpatterns = [
    path('dejeuner/', dejeuner, name='dejeuner'),
]
