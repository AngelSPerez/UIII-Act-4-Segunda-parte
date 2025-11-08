from django.shortcuts import render, redirect, get_object_or_404
# Importamos el modelo Categoria
from .models import Producto, Categoria

# NUEVA VISTA para la página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# --- VISTAS DE PRODUCTO (Existentes) ---

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/ver_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        precio_venta = request.POST.get('precio_venta')
        stock = request.POST.get('stock', 0)
        codigo_barras = request.POST.get('codigo_barras', '')
        categoria_id = request.POST.get('categoria')
        producto = Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio_venta=precio_venta,
            stock=stock,
            codigo_barras=codigo_barras,
            categoria_id=categoria_id
        )
        return redirect('ver_productos')
    # NOTA: Deberías pasar las categorías al template para el <select>
    # categorias = Categoria.objects.all()
    # return render(request, 'producto/agregar_producto.html', {'categorias': categorias})
    return render(request, 'producto/agregar_producto.html')

def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre', producto.nombre)
        producto.descripcion = request.POST.get('descripcion', producto.descripcion)
        producto.precio_venta = request.POST.get('precio_venta', producto.precio_venta)
        producto.stock = request.POST.get('stock', producto.stock)
        producto.codigo_barras = request.POST.get('codigo_barras', producto.codigo_barras)
        # Faltaría actualizar categoría y proveedor si lo permites en el form
        producto.save()
        return redirect('ver_productos')
    # NOTA: También deberías pasar las categorías aquí
    # categorias = Categoria.objects.all()
    # return render(request, 'producto/actualizar_producto.html', {'producto': producto, 'categorias': categorias})
    return render(request, 'producto/actualizar_producto.html', {'producto': producto})

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})


# --- NUEVAS VISTAS DE CATEGORIA ---

def ver_categorias(request):
    """Muestra todas las categorías."""
    categorias = Categoria.objects.all()
    return render(request, 'categoria/ver_categorias.html', {'categorias': categorias})

def agregar_categoria(request):
    """Agrega una nueva categoría."""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        pasillo_str = request.POST.get('pasillo')
        responsable_area = request.POST.get('responsable_area', '')
        # Si el checkbox está marcado, request.POST.get('activa') será 'on'
        activa = request.POST.get('activa') == 'on' 

        # Convertir pasillo a Integer, manejando None o string vacío
        pasillo = None
        if pasillo_str and pasillo_str.isdigit():
            pasillo = int(pasillo_str)

        Categoria.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            pasillo=pasillo,
            responsable_area=responsable_area,
            activa=activa
        )
        return redirect('ver_categorias')
    return render(request, 'categoria/agregar_categoria.html')

def actualizar_categoria(request, categoria_id):
    """Actualiza una categoría existente."""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre', categoria.nombre)
        categoria.descripcion = request.POST.get('descripcion', categoria.descripcion)
        
        pasillo_val = request.POST.get('pasillo', categoria.pasillo)
        if pasillo_val == '': # Si el usuario borró el número
            categoria.pasillo = None
        elif str(pasillo_val).isdigit():
            categoria.pasillo = int(pasillo_val)
        # Si no es dígito o vacío, simplemente mantiene el valor original (categoria.pasillo)
            
        categoria.responsable_area = request.POST.get('responsable_area', categoria.responsable_area)
        # Si el checkbox no está marcado, .get('activa') será None, y (None == 'on') es False
        categoria.activa = request.POST.get('activa') == 'on'
        
        categoria.save()
        return redirect('ver_categorias')
    return render(request, 'categoria/actualizar_categoria.html', {'categoria': categoria})

def borrar_categoria(request, categoria_id):
    """Borra una categoría."""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('ver_categorias')
    return render(request, 'categoria/borrar_categoria.html', {'categoria': categoria})