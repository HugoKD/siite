"""bde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import equipe, pougnes, contact, programme, index, dejeuner, clique, partenaire

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),
    path("lequipe/", equipe, name="equipe"),
    path("pougnes/", pougnes, name="pougnes"),
    path("programme/", programme, name="programme"),
    path("devenir-partenaire/", contact, name="contact"),
    path("dejeuner/", dejeuner, name="dejeuner"),
    path("clique/", clique, name="clique"),
    path("nos-partenaires/", partenaire, name="partenaire"),
]
