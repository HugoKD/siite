from django.shortcuts import render


def index(request):
    return render(request, "bde/index.html")

def equipe(request):
    return render(request, "bde/equipe.html")

def pougnes(request):
    return render(request, "bde/pougnes.html")

def contact(request):
    return render(request, "bde/contact.html")

def programme(request):
    return render(request, "bde/programme.html")


def clique(request):
    return render(request, "bde/clique.html")

def partenaire(request):
    return render(request, "bde/partenaire.html")