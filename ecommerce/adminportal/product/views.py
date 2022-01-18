from audioop import reverse
from django.contrib.messages.api import add_message, success
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured

# Create your views here.
class ProductCreateView(CreateView):
    form_class = ProductAddForm
    model = Product
    template_name = "adminportal/product_creation.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            if 'image' in request.FILES:
                product.image = request.FILES['image']
            product.save()
            registered = True
            messages.success(request, 'Product was created successfully!')

            return redirect('user_urls:admin_customized')

class BrandCreateView(CreateView):
    form_class = ProductBrandForm
    model = Brand
    template_name = "adminportal/brand.html"
  
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            brand = form.save()
            brand.save()
            messages.success(request, 'Brand was created successfully!')

            return redirect('user_urls:admin_customized')


class CategoryCreateView(CreateView):
    form_class = ProductCategoryForm
    model = Category
    template_name = "adminportal/category.html"
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            category = form.save()
            category.save()
            messages.success(request, 'Category was created successfully!')

            return redirect('user_urls:admin_customized')

class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductAddForm
    template_name = 'adminportal/update.html'

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'adminportal/proddel.html'
    context_object_name = 'delete_product'

    def get_success_url(self):
        return reverse('user_urls:admin_customized')
