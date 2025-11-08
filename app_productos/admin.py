from django.contrib import admin
# Importamos los modelos faltantes
from .models import Producto, Categoria, Proveedor

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_venta', 'stock', 'categoria')
    search_fields = ('nombre', 'codigo_barras')
    list_filter = ('categoria',)

# NUEVO: Registro para Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pasillo', 'responsable_area', 'activa')
    search_fields = ('nombre', 'responsable_area')
    list_filter = ('activa', 'pasillo')

# NUEVO: Registro básico para Proveedor
admin.site.register(Proveedor)