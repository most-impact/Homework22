from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """
    Получает список всех продуктов из кэша или базы данных
    """
    products = Product.objects.select_related('category', 'owner').all()
    return products

def get_products_by_category(category_id):
    """
    Получает список всех продуктов в указанной категории
    """
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)
    
    key = f"products_by_category_{category_id}"
    products = cache.get(key)
    if products is not None:
        return products
    
    products = Product.objects.filter(category_id=category_id)
    cache.set(key, products)
    return products