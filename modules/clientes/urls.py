from django.urls import path
from modules.clientes.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]