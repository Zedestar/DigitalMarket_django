from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'myapp/index.html', context=context)


def detail_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product' : product
    }
    return render(request, 'myapp/view.html', context=context)