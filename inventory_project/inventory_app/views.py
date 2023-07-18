from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Category, Provider
from .forms import ProductForm, CategoryForm, ProviderForm

carrito = []

def product_list(request):
    search_query = request.GET.get('search')
    products = Product.objects.all()

    if search_query:
        products = products.filter(name__icontains=search_query)

    paginator = Paginator(products, 7)
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

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_create')
    else:
        form = CategoryForm()
    categories = Category.objects.all()
    return render(request, 'inventory_app/category_create.html', {'form': form, 'categories': categories})

def provider_create(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('provider_create')
    else:
        form = ProviderForm()
    providers = Provider.objects.all()
    return render(request, 'inventory_app/provider_create.html', {'form': form, 'providers': providers})

def compra(request):
    products = Product.objects.all()
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'inventory_app/compra.html', {'page_obj': page_obj})

def agregar_al_carrito(request, pk):
    product = Product.objects.get(pk=pk)
    carrito.append(product)
    return redirect('ver_carrito')

def ver_carrito(request):
    total = sum(item.price * item.quantity for item in carrito)
    return render(request, 'inventory_app/agregar_al_carrito.html', {'carrito': carrito, 'total': total})

def realizar_compra(request):
    for item in carrito:
        quantity_input = int(request.POST.get('quantity_{}'.format(item.pk), 0))
        if quantity_input > 0:
            quantity_difference = item.quantity - quantity_input
            if quantity_difference >= 0:
                item.quantity = quantity_difference
                item.save()
            else:
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

def login(request):
    return render(request, 'inventory_app/login.html')