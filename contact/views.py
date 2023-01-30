from django.shortcuts import render
from .models import ContactModel
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