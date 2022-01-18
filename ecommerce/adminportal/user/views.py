from distutils.log import error
import imp
from multiprocessing import context
from re import template
from statistics import mode
from django.db.models.query_utils import Q
from adminportal.product.models import *
from django.http.response import  HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, View, ListView, DeleteView, UpdateView,RedirectView, DetailView, FormView
from django.contrib.auth.views import LoginView
from .forms import   UserForm
from django.contrib.auth.models import User
from .models import *
from adminportal.product.models import Product
# Create your views here.

class AdminUserView(ListView):
    model = User 
    template_name = 'adminportal/user.html'
    context_object_name = 'user_data'

    

class HomeView(ListView):

    context_object_name = 'items'
    model = Product
    # model = models.ProductImage
    template_name = 'userportal/index.html'

class AdminHomeView(ListView):

    context_object_name = 'items'
    model = Product
    # model = models.ProductImage
    template_name = 'adminportal/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.all()
        return context
    
   

class SingleProductView(DetailView):
    model = Product
    template_name = 'userportal/single_product.html'

    
class SearchView(ListView):

    model = Product
    template_name = 'userportal/search.html'
    context_object_name = 'products'
    # context_object_name = 'q'

    def get_queryset(self):
        print("enter the function")
        q = self.request.GET.get('q')
        print("getting q", q)
        data = dict()
        try:
            products = Product.objects.filter(Q(name__icontains=q) | Q(price__icontains=q))
            data['products'] = products 
            data['q'] = q
            print('data', data)
            return products
        except:
            return q 

class SignUpView(LoginView):
    template_name = 'adminportal/login.html'
    redirect_authenticated_user = True
 

    def get_success_url(self):
        return reverse('user_urls:index')

       
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:    
    #         return super().dispatch(request, *args, **kwargs)
    #     else:
    #         return redirect("user_urls:index")


    # def post(self, request, *args, **kwargs):
    #     try:
    #         print("Entering Username nd Password")
    #         username = request.POST.get('username')
    #         password = request.POST.get('password')

    #         user = authenticate(username=username, password=password)
    #         print("user", user)
    #         token, created = Token.objects.get_or_create(user=user)

    #         if user:
    #             if user.is_active:
    #                 login(request, user)
    #                 return HttpResponseRedirect(reverse("user_urls:index"))

    #             else:
    #                 return HttpResponse("Account not active")

    #     except Exception as e:
    #         messages.add_message(request, messages.INFO, "Please Enter Valid Username or Password")
    #         return render(request, 'adminportal/login.html', {})


class RegisterUser(FormView):
    form_class = UserForm
    template_name = 'adminportal/registration.html'
  

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)   
        user.save()    
        print("user is saving data")
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        form = self.form_class()
        print("Data is invalid") 
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('user_urls:login_1')


        
    
class UpdateUser(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'adminportal/update.html'

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
    

