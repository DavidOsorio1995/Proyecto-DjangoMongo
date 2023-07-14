from django import forms
from .models import Product
from .models import Proveedor
from .models import Categorias

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'
