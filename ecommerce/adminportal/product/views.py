from django.urls import reverse
from django.contrib.messages.api import add_message, success
from django.http import request
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import *
from django.shortcuts import get_object_or_404
# from ecommerce.adminportal.product.models import ProductImage
from django.db.models.query_utils import Q

# Create your views here.
class ProductCreateView(SuccessMessageMixin, CreateView):
    form_class = ProductAddForm
    model = Product
    template_name = "adminportal/product_creation.html"
    
    def get_success_message(self, cleaned_data):
        name = cleaned_data['name']
        return  name + " Created Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

class BrandCreateView(SuccessMessageMixin, CreateView, ListView):
    form_class = ProductBrandForm
    model = Brand
    template_name = "adminportal/brand.html"
    # success_url = '/admin_customized/'
    context_object_name = 'brand'

    def get_success_message(self, cleaned_data):
        name = cleaned_data["name"]
        return name + " Created Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')
     
class CategoryCreateView(SuccessMessageMixin, CreateView, ListView):
    form_class = ProductCategoryForm
    model = Category
    template_name = "adminportal/category.html"
    # success_message = "%(name)s was created successfully"
    context_object_name = 'category'

    def get_success_message(self, cleaned_data):
        name = cleaned_data["name"]
        return name + " Created Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized') 

class UpdateProduct(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductAddForm
    template_name = 'adminportal/update.html'
    success_url = '/admin_customized/'

    def get_success_message(self, cleaned_data):
        name = cleaned_data["name"]
        return name + " Updated Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

class DeleteProduct(SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'adminportal/proddel.html'
    context_object_name = 'delete_product'

    def get_success_message(self, cleaned_data):
        return "Product Deleted Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

class UpdateBrandView(SuccessMessageMixin, UpdateView):
    model = Brand
    form_class = ProductBrandForm
    template_name = 'adminportal/update.html'
    success_url = '/admin_customized/'

    def get_success_message(self, cleaned_data):
        name = cleaned_data["name"]
        return name + " Updated Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

class DeleteBrandView(SuccessMessageMixin, DeleteView):
    model = Brand
    template_name = 'adminportal/proddel.html'
    context_object_name = 'delete_product'

    def get_success_message(self, cleaned_data):
        return "Brand Deleted Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

class UpdateCategoryView(SuccessMessageMixin, UpdateView):
    model = Category
    form_class = ProductCategoryForm
    template_name = 'adminportal/update.html'
    success_url = '/admin_customized/'

    def get_success_message(self, cleaned_data):
        self.name = cleaned_data["name"]
        return self.name + " Updated Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

class DeleteCategoryView(SuccessMessageMixin, DeleteView):
    model = Category
    template_name = 'adminportal/proddel.html'
    context_object_name = 'delete_product'

    def get_success_message(self, cleaned_data):
        return "Category Deleted Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

class CategoryBrandListView(ListView):
    model = Product
    # model = models.ProductImage
    context_object_name = 'products'
    template_name = 'userportal/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.all()
        context["category"] = Category.objects.all()
        return context 

class CategoryFilterView(ListView):
    model = Product
    template_name = 'userportal/category.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.all()
        context["category"] = Category.objects.all()
        return context 

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        # brand = get_object_or_404 (Brand, pk = self.kwargs['pk'])
        print("category", category)
        # print("brand", brand)
        if category:
            products = Product.objects.filter(Q(category__name = category))
            print("Inside Queryset")
            # products = Product.objects.filter(Q(brand__name = slug) | Q(category__name = slug))
        else:
            products = Product.objects.none()
        print("Products", products)
        return products  

class BrandFilterView(ListView):
    model = Product
    template_name = 'userportal/category.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.all()
        context["category"] = Category.objects.all()
        return context 

    def get_queryset(self):
        brand = get_object_or_404(Brand, pk=self.kwargs['pk'])
        # brand = get_object_or_404 (Brand, pk = self.kwargs['pk'])
        print("brand", brand)
        # print("brand", brand)
        if brand:
            products = Product.objects.filter(Q(brand__name = brand))
            print("Inside Queryset")
            # products = Product.objects.filter(Q(brand__name = slug) | Q(category__name = slug))
        else:
            products = Product.objects.none()
        print("Products", products)
        return products  


 # def form_valid(self, form):
    #     product = form.save()
    #     if 'image' in request.FILES:
    #         ProductImage(
    #             product = product,
    #             image= image
    #         )
    #         product.image = request.FILES['image']
    #         ProductImage.save()
    #     return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         product = form.save()
    #         if 'image' in request.FILES:
    #             product.image = request.FILES['image']
    #         product.save()
    #         registered = True
    #         messages.success(request, 'Product was created successfully!')

    #         return redirect('user_urls:admin_customized')