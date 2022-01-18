from django import forms
from django.forms import fields, models

from .models import Brand, Category, Product

class ProductAddForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        # widgets = {'name': forms.CharField(attrs = {'class': 'form-group',
        #                                             'id' : 'name',
        #                                             'name': 'product_name',})}
    # def clean_
class ProductBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
    
class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'