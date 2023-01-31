from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ContactModel


def dejeuner(request):
    if request.method == 'POST':
            nom= request.POST.get('Nom')
            prenom= request.POST.get('Prenom')
            adresse= request.POST.get('Adresse')
            message= request.POST.get('Message')
            vieux=request.POST.get('Vieux')
            couvert=request.POST.get('Couvert')
            menu=request.POST.get('Menu')
            num = request.POST.get('Num')
            horaire = request.POST.get('Horaire')

            Users = ContactModel.objects.all()

            if vieux=='on':
                vieux=True;
            elif vieux=='None':
                vieux=False;
            if couvert=='on':
                couvert=True
            elif couvert=='None':
                couvert=False

            list_prenom, list_nom = ['pivot'], ['pivot']
            for i in Users:
                list_prenom.append(i.Prenom)
                list_nom.append(i.Nom)
            for i in range(0,len(list_nom)):
                if nom == list_nom[i]:
                    for j in range(0,len(list_prenom)):
                        if list_prenom[j]==prenom:
                            return HttpResponseRedirect('/erreur1/')
                            break
            #dernier test :
            print(list_prenom)
            list_prenom.append(nom)
            list_nom.append(prenom)
            NewComamande= ContactModel.objects.create(Nom= nom, Prenom=prenom, Adresse=adresse, Message=message, Vieux=vieux,Couvert=couvert,Horaire=horaire, Menu=menu, Num= num)
            NewComamande.save()

            #form.save()
            return HttpResponseRedirect('/redirection/')


    return render(request, "dejeuner/dejeuner.html")

def redirection(request):
    return render(request, "dejeuner/redirection.html")

def erreur1(request):
    return render(request, "dejeuner/erreur1.html")
