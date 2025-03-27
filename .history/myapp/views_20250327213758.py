from django.shortcuts import render
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
    form = ProductForm()
    context = {
        "form" : form,
    }
    return render(request, 'myapp/create_product.html', context=context)