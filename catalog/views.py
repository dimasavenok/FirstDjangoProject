from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Product


# Create your views here.


class HomeView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Skystore"
        return context


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Skystore"
        return context


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "catalog/product.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Skystore"
        return context