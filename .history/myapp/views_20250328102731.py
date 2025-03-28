from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'myapp/index.html', context=context)


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product' : product
    }
    return render(request, 'myapp/product_details.html', context=context)


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully")
            return redirect("index_view")
    else:      
        form = ProductForm()
    context = {
        "form" : form,
    }
    return render(request, 'myapp/create_product.html', context=context)


def edit_product(request, pk):
    product_to_edit = Product.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product_to_edit)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully")
            return redirect("index_view")
        else:
            messages.error(request, f"{form.errors}")
    else:
        form = ProductForm(instance=product_to_edit)
    context = {
        "form":form
    }
    return render(request, 'myapp/edit_product.html', context=context)