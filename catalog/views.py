from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.
def home(request):
    context = {
        "title": "Skystore",
        "products": Product.objects.all()
    }
    return render(request, "catalog/home.html", context=context)

def contacts(request):
    return render(request, "catalog/contacts.html")

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "title": f"Skystore - {product.name}",
        "product": product
    }
    return render(request, "catalog/product.html", context=context)