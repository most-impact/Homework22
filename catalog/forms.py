from django import forms
from .models import Product

prohibited_words = [
    'обман', 'радар', 'бесплатно', 'биржа', 'полиция',
    'казино', 'дешево', 'криптовалюта', 'крипта'
]


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data.get('name', '').lower()
        if any(word in name for word in prohibited_words):
            raise forms.ValidationError("Название содержит запрещённые слова.")
        return self.cleaned_data['name']

    def clean_description(self):
        description = self.cleaned_data.get('description', '').lower()
        if any(word in description for word in prohibited_words):
            raise forms.ValidationError("Описание содержит запрещённые слова.")
        return self.cleaned_data['description']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'category', 'price']