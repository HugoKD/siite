from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import PlaceDispo, ContactModel


def dejeuner(request):

    horaires=PlaceDispo.objects.all()

    context = {
        'horaires': horaires,
    }

    if request.method == 'POST':
            nom= request.POST.get('Nom')
            prenom= request.POST.get('Prenom')
            adresse= request.POST.get('Adresse')
            message= request.POST.get('Message')
            vieux=request.POST.get('Vieux')
            couvert=request.POST.get('Couvert')
            menu=request.POST.get('Menu')
            num = request.POST.get('Num')
            boisson= request.POST.get('Boisson')
            horaire = request.POST.get('Horaire')


            Users = ContactModel.objects.all()
            Horaire_list = PlaceDispo.objects.all()

            for i in Horaire_list:
                if i.Horaire==horaire:
                    i.Count-=1
                    i.save()
                    break

            if vieux=='on':
                vieux=True
            elif vieux==None:
                vieux=False
            if couvert=='on':
                couvert=True
            elif couvert==None:
                couvert=False

            list_prenom, list_nom = ['PiVoT'], ['PiVoT']
            #fonction qui enleve les majuscules dans les strings

            for i in Users:
                list_prenom.append(i.Prenom.lower())
                list_nom.append(i.Nom.lower())
            for i in range(0,len(list_nom)):
                if nom.lower() == list_nom[i]:
                    for j in range(0,len(list_prenom)):
                        if list_prenom[j]==prenom.lower():
                            return HttpResponseRedirect('/erreur1/')
                            break

            #dernier test --> matcher liste prénoms + nom école : fait ok

            NewComamande= ContactModel.objects.create(Nom= nom, Prenom=prenom, Adresse=adresse, Message=message, Vieux=vieux,Couvert=couvert,Horaire=horaire, Menu=menu, Num= num, Boisson=boisson)
            NewComamande.save()

            #form.save()
            return HttpResponseRedirect('/redirectionDej/')


    return render(request, "dejeuner/dejeuner.html", context)

def redirection(request):
    return render(request, "dejeuner/redirection.html")

def erreur1(request):
    return render(request, "dejeuner/erreur1.html")

def menu(request):
    return render(request, "dejeuner/menu.html")

