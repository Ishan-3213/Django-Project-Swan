from django.urls import reverse
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from adminportal.product.models import Product
from adminportal.product.forms import ProductAddForm
# Create your views here.

#--------------------Product Base Class-------------------------#
class BaseCreateView(SuccessMessageMixin, CreateView, ListView):
    model = Product
    form_class = ProductAddForm
    template_name = "adminportal/product_creation.html"
 
    def get_success_message(self, cleaned_data):
        self.name = cleaned_data['name']
        return self.name + " Created Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

class BaseUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductAddForm
    template_name = 'adminportal/update.html'
    # success_url = '/admin_customized/'

    def get_success_message(self, cleaned_data):
        self.name = cleaned_data["name"]
        return self.name + " Updated Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

class BaseDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'adminportal/proddel.html'
    context_object_name = 'delete_product'

    def get_success_message(self, cleaned_data):
        return "Product Deleted Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:admin_customized')

#--------------------User Base Class-------------------------#
class BaseListView(LoginRequiredMixin, ListView):
    pass

class BaseDetailView(LoginRequiredMixin,DetailView):
    pass

