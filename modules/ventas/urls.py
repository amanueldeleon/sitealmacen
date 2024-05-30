from django.urls import path
from modules.ventas.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]