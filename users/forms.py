from django.contrib.auth.forms import UserCreationForm

from catalog.forms import ProductForm
from models import User


class UserRegisterForm(ProductForm, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
