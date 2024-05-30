from django.urls import path
from modules.productos.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]