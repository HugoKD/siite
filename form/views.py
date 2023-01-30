from django.shortcuts import render
from .form import ContactForm
from django.http import HttpResponseRedirect

def dejeuner(request):
    if request.method == 'POST':
            name= request.POST.get()

            form.save()
            return HttpResponseRedirect('/redirection/')

    else:
        form = ContactForm()

    return render(request, "form/dejeuner.html", {'form' : form})

def redirection(request):
    return render(request, "form/redirection.html")