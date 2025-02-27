from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (HomeTemplateView, ContactTemplateView, ProductDetailView, ProductListView, ProductCreateView,
                           ProductUpdateView, ProductDeleteView, ProductsByCategoryListView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:category_id>/products/', ProductsByCategoryListView.as_view(), name='products_by_category'),
]
