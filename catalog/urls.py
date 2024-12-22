from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (HomeTemplateView, ContactTemplateView, ProductDetailView, ProductListView, ProductCreateView,
                           ProductUpdateView, ProductDeleteView)
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]