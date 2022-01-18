from django.db.models.query_utils import Q
from adminportal.product.models import *
from django.http.response import   HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import   UserForm
from django.contrib.auth.models import User
from .models import *
from adminportal.product.models import Product
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class AdminUserView(LoginRequiredMixin,ListView):
    model = User 
    template_name = 'adminportal/user.html'
    context_object_name = 'user_data'

class HomeView(ListView):

    context_object_name = 'items'
    model = Product
    # model = models.ProductImage
    template_name = 'userportal/index.html'

class AdminHomeView(LoginRequiredMixin, ListView):

    context_object_name = 'items'
    model = Product
    # model = models.ProductImage
    template_name = 'adminportal/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.all()
        return context   
   
class SingleProductView(LoginRequiredMixin,DetailView):
    model = Product
    template_name = 'userportal/single_product.html'


class SearchView(LoginRequiredMixin,ListView):

    model = Product
    template_name = 'userportal/search.html'
    context_object_name = 'products'
    # context_object_name = 'q'

    def get_queryset(self):
        search = self.request.GET.get('q')
        if search:
            products = Product.objects.filter(Q(name__icontains=search ) | Q(price__icontains=search) |
                                             Q(brand__name=search) | Q(category__name=search)).order_by('created_at')
        else:
            products = Product.objects.none()
        return products

class RegisterUser(FormView, SuccessMessageMixin):
    form_class = UserForm
    template_name = 'adminportal/registration.html'
    success_message = "%(name)s was created successfully"
  

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)   
        user.save()    
        print("user is saving data")
        return super().form_valid(form)

    def form_invalid(self, form):
        form = self.form_class()
        print("Data is invalid") 
        return super().form_invalid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + " Created Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:login_1')

    
class UpdateUser(UpdateView, SuccessMessageMixin):
    model = User
    form_class = UserForm
    template_name = 'adminportal/update.html'
    success_message = "%(username)s was created successfully"

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)   
        user.save()    
        print("user is saving data")
        return HttpResponseRedirect(self.get_success_url())

    # def form_invalid(self, form):
    #     form = self.form_class()
    #     print("Data is invalid") 
    #     return super().form_invalid(form)

    def get_success_url(self):
        return reverse('user_urls:user_data')


class DeleteUser(DeleteView):
    model = User
    template_name = 'adminportal/proddel.html'
    context_object_name = 'delete_product'

    def get_success_url(self):
        return reverse('user_urls:user_data')



    # def get_context_data(self,  **kwargs):
    #     context = super(UpdateUser, self).get_context_data(**kwargs)
    #     context['customer'] = Customer.objects.get(id =0)
    #     if 'form_U' not in context:
    #         context['form_U'] = self.form_class(initial={'username': context['user'].username , 'password': context['user'].password})
    #     if 'form_P' not in context:
    #         context['form_P'] = self.second_form_class(initial={'email': context['customer'].email, 'phone_number' : context['customer'].phone_number})
    #     return context





    # def get_context_data(self, **kwargs):
    #     context = super(UpdateUser, self).get_context_data(**kwargs)
    #     if 'form_U' not in context:
    #         context['form_U'] = self.form_class(self.request.GET , instance=self.request.user)
    #     if 'form_P' not in context:
    #         context['form_P'] = self.second_form_class(self.request.GET, instance=self.request.user)
    #     return context




    # def get(self, request, *args, **kwargs):
    #     super(UpdateUser, self).get(request, *args, **kwargs)
    #     form = self.form_class
    #     form2 = self.second_form_class
    #     return self.render_to_response(self.get_context_data(
    #         object=self.object, form=form, form2=form2))

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.form_class(request.POST)
    #     form2 = self.second_form_class(request.POST)

    #     if form.is_valid() and form2.is_valid():
    #         userdata = form.save(commit=False)
    #         # used to set the password, but no longer necesarry
    #         userdata.save()
    #         employeedata = form2.save(commit=False)
    #         employeedata.user = userdata
    #         employeedata.save()
    #         messages.success(self.request, 'Settings saved successfully')
    #         return HttpResponseRedirect(self.get_success_url())
    #     else:
    #         return self.render_to_response(
    #           self.get_context_data(form=form, form2=form2))
    

