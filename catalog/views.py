from django.shortcuts import render

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