from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import PlaceDispo, ContactModel
from openpyxl import load_workbook
import os

def dejeuner(request):

    horaires=PlaceDispo.objects.all()

    context = {
        'horaires': horaires,
    }

    if request.method == 'POST':
            nom= request.POST.get('Nom').lower()
            prenom= request.POST.get('Prenom').lower()
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
                list_prenom.append(i.Prenom)
                list_nom.append(i.Nom)
            for i in range(0,len(list_nom)):
                if nom.lower() == list_nom[i]:
                    for j in range(0,len(list_prenom)):
                        if list_prenom[j]==prenom.lower():
                            return HttpResponseRedirect('/erreur1/')
                            break

            #dernier test --> matcher liste prénoms + nom école : fait ok

            wb = load_workbook('Dejeuner/petitdej.xlsx')
            ws = wb[f'{horaire}']
            ws[f'A{ws["L1"].value}'].value = adresse
            ws[f'B{ws["L1"].value}'].value = 'Evry'
            ws[f'C{ws["L1"].value}'].value = 91000
            ws[f'D{ws["L1"].value}'].value = prenom
            ws[f'E{ws["L1"].value}'].value = nom
            ws[f'F{ws["L1"].value}'].value = num
            ws[f'G{ws["L1"].value}'].value = vieux
            ws[f'H{ws["L1"].value}'].value = couvert
            ws[f'I{ws["L1"].value}'].value = menu
            ws[f'J{ws["L1"].value}'].value = boisson
            ws[f'K{ws["L1"].value}'].value = message

            ws['L1'].value += 1

            wb.save('Dejeuner/petitdej.xlsx')


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

