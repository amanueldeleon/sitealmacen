from django.contrib import admin
from modules.ventas.models import Venta, VentaProducto

class VentaProductoInline(admin.TabularInline):
	model = VentaProducto
	extra = 1

class VentaAdmin(admin.ModelAdmin):
	inlines = (VentaProductoInline,)
	list_display = ('fecha', 'descuento', 'total', 'subtotal', 'usuario', 'cliente', 'created', 'updated')
	list_filter = ('fecha', 'usuario', 'cliente')
	search_fields = ('usuario_username', 'cliente_nombreCliente')
    
class VentaProductoAdmin(admin.ModelAdmin):
	list_display = ('producto', 'venta', 'fechaVenta', 'precio', 'cantidad', 'total')
	list_filter = ('producto', 'venta', 'fechaVenta')
	search_fields = ('producto_nombre', 'ventausuario_username')

admin.site.register(Venta, VentaAdmin)
