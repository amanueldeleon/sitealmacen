from django.contrib import admin
from modules.productos.models import Producto, TipoProducto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'precio')
    ordering = ('nombre', 'marca', 'precio')
    search_fields = ('nombre', 'marca', 'precio')

class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    ordering = ('nombre', )
    search_fields = ('nombre',)

admin.site.register(TipoProducto,TipoProductoAdmin)
admin.site.register(Producto, ProductoAdmin)