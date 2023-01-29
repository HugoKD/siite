from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from .forms import UserLoginForm
from bde.views import index
from .views import register

app_name = 'accounts'


urlpatterns = [
    path('login/', views.LoginView.as_view(template_name="accounts/login.html", redirect_authenticated_user=True, authentication_form=UserLoginForm), name='login'),
    path('logout/', views.LogoutView.as_view(template_name="accounts/logout.html", next_page=index), name='logout'),
    path('register/', register, name='register'),
]