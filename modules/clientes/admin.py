from django.contrib import admin
from modules.clientes.models import Cliente

# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombreCliente', 'direccionCliente', 'telefonoCliente')
    ordering = ('nombreCliente', 'direccionCliente', 'telefonoCliente')
    search_fields = ('nombreCliente', 'direccionCliente', 'telefonoCliente')
    


admin.site.register(Cliente, ClienteAdmin)