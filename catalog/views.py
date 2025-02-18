from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm, ProductModeratorForm

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(LoginRequiredMixin, ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_edit_name') and user.has_perm('catalog.can_edit_description'):
            return ProductModeratorForm
        raise PermissionDenied()


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
