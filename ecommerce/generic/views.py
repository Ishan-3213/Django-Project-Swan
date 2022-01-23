from pyexpat import model
from re import template
from django.views.generic import  ListView

from adminportal.product.models import Brand, Category, Product
# Create your views here.

class BaseListView(ListView):
    model = Product
    template_name = 'userportal/category.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.all()
        context["category"] = Category.objects.all()
        return context 