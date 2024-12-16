from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def product_list(request):
    product = Product.objects.all()
    context = {"products": product}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"products": product}
    return render(request, 'product_detail.html', context)
