from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache

from catalog.services import get_products_from_cache


def my_view(request):
    data = cache.get('my_key')

    if not data:
        data = 'some expensive computation'
        cache.set('my_key', data, 60 * 15)

    return HttpResponse(data)


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.object.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user()
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_edit_product") and user.has_perm("catalog.can_edit_descriptions"):
            return ProductModeratorForm
        raise PermissionDenied()


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')