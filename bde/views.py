from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, "bde/index.html")

def equipe(request):
    return render(request, "bde/equipe.html")

def pougnes(request):
    return render(request, "bde/pougnes.html")

def programme(request):
    return render(request, "bde/programme.html")

def dejeuner(request):
    return render(request, "bde/dejeuner.html")

def clique(request):
    return render(request, "bde/clique.html")

def partenaire(request):
    return render(request, "bde/partenaire.html")