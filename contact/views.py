import datetime

from django.shortcuts import render
from django.utils import timezone

from .models import ContactModel
from django.db.models.functions import Now

# Create your views here.
def contact(request):
    if request.method =='POST':

        name=request.POST.get('Name')
        mail = request.POST.get('Mail')
        objet = request.POST.get('Object')
        message = request.POST.get('Message')
        NewUser= ContactModel.objects.create(Nom=name,Mail=mail,Objet=objet,Message=message)
        print(NewUser)
        NewUser.save()
    #(request.POST.get('name')) accede à la valeur name de la resuquestr
    return render(request, "contact/contact.html")