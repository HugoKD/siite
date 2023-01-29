from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from astrocoins.models import Classement
from django.contrib.auth.models import User


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

def dejeuner(request):
    return render(request, "bde/dejeuner.html")

def clique(request):
    return render(request, "bde/clique.html")

def partenaire(request):
    return render(request, "bde/partenaire.html")

@login_required
def astrocoins(request):
    classements = Classement.objects.all().order_by('-points')
    user_email = request.user.email
    i=1
    context = {}
    somme = 0
    for classement in classements:
        classement.rang = i
        classement.save()
        somme += classement.points
        i+=1
    for classement in classements:
        if classement.email == user_email:
            user_auth = classement
            context['user_auth'] = user_auth
            context['classements'] = classements
            break
        else:
            context['classements'] = classements
    context['total']=somme
    return render(request, 'bde/astrocoins.html', context)