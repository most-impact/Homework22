from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_list, product_detail
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail')
]