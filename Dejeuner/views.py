from django.shortcuts import render

# Create your views here.
def dejeuner(request):
    return render(request, "dejeuner/dejeuner.html")
