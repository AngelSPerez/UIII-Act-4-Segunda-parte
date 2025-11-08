from django.urls import path
from . import views

urlpatterns = [
    # Ruta raíz ahora apunta a la vista de inicio
    path('', views.inicio, name='inicio'), 
    
    # --- RUTAS DE PRODUCTOS ---
    path('productos/', views.ver_productos, name='ver_productos'), 
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/<int:producto_id>/editar/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/<int:producto_id>/borrar/', views.borrar_producto, name='borrar_producto'),

    # --- NUEVAS RUTAS DE CATEGORIAS ---
    path('categorias/', views.ver_categorias, name='ver_categorias'),
    path('categorias/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categorias/<int:categoria_id>/editar/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categorias/<int:categoria_id>/borrar/', views.borrar_categoria, name='borrar_categoria'),
]