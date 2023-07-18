from django import forms
from .models import Product, Category, Provider

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
