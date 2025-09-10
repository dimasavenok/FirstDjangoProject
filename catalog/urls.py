from django.urls import path
from catalog import views
from catalog.views import (
    HomeView, ContactsView, ProductDetailView,
    ProductCreateView, ProductDeleteView, ProductUpdateView, unpublish_product, ProductByCategoryView
)

app_name = "catalog"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<int:category_id>', ProductByCategoryView.as_view(), name="category"),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/unpublish/', unpublish_product, name='product_unpublish'),
]