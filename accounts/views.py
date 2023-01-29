from django.shortcuts import render, redirect
from bde import views
from .forms import UserForm
from astrocoins.models import Classement
from django.contrib.auth import views
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login
from bde.views import astrocoins


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            password = request.POST['password1']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user = authenticate(request, email=email, password=password, first_name=first_name, last_name=last_name)
            if user is not None:
                login(request, user)
                new = Classement(email=request.user.email, prenom=request.user.first_name, nom=request.user.last_name,points=0, rang=0)
                new.save()
            else:
                print('no')
            if request.user.is_authenticated:
                return redirect(astrocoins)
    else:
        form = UserForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)


