from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product
from .models import Proveedor
from .models import Categorias
from .forms import ProductForm
from .forms import CategoriasForm
from .forms import ProveedorForm


carrito = []

def product_list(request):
    search_query = request.GET.get('search')
    products = Product.objects.all()

    if search_query:
        products = products.filter(name__icontains=search_query)

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'inventory_app/product_list.html', {'page_obj': page_obj, 'search_query': search_query})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory_app/product_create.html', {'form': form})

def proveedor_create(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProveedorForm()
    return render(request, 'inventory_app/proveedor_create.html', {'form': form})

def categoria_create(request):
    if request.method == 'POST':
        form = CategoriasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = CategoriasForm()
    return render(request, 'inventory_app/categoria_create.html', {'form': form})

def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory_app/product_update.html', {'form': form, 'product': product})

def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product_list')

def compra(request):
    products = Product.objects.all()
    paginator = Paginator(products, 9)  # Mostrar 9 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'inventory_app/compra.html', {'page_obj': page_obj})

def agregar_al_carrito(request, pk):
    product = Product.objects.get(pk=pk)
    carrito.append(product)
    return redirect('ver_carrito')

def ver_carrito(request):
    total = sum(item.precio * item.cantidad for item in carrito)
    return render(request, 'inventory_app/agregar_al_carrito.html', {'carrito': carrito, 'total': total})


def realizar_compra(request):
    for item in carrito:
        cantidad_input = int(request.POST.get('cantidad_{}'.format(item.pk), 0))
        if cantidad_input > 0:
            cantidad_difference = item.cantidad - cantidad_input
            if cantidad_difference >= 0:
                item.cantidad = cantidad_difference
                item.save()
            else:
                # Si la cantidad ingresada es mayor que la cantidad en la base de datos, puedes tomar una acción adecuada
                # como mostrar un mensaje de error o ajustar la lógica según tus necesidades.
                pass
        else:
            item.delete()

    carrito.clear()
    return render(request, 'inventory_app/compra_confirmada.html')

def compra_confirmada(request):
    return render(request, 'inventory_app/compra_confirmada.html')

def quitar_del_carrito(request, pk):
    product = Product.objects.get(pk=pk)
    carrito.remove(product)
    return redirect('ver_carrito')

