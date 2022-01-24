from django.db.models.query_utils import Q
from django.http import JsonResponse
from django.shortcuts import render
from adminportal.product.models import *
from django.urls import reverse
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import   UserForm
from django.contrib.auth.models import User
from .models import *
from adminportal.product.models import Product
from django.contrib.messages.views import SuccessMessageMixin

# Create BaseView For the below classes 
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

class SearchView(LoginRequiredMixin,ListView):

    model = Product
    template_name = 'userportal/search.html'
    context_object_name = 'products'
    # context_object_name = 'q'

    def get_queryset(self):
        search = self.request.GET.get('q')
        print("search", search)
        if search:
            products = Product.objects.filter(Q(name__icontains=search ) | Q(price__icontains=search) |
                                             Q(brand__name=search) | Q(category__name=search)).order_by('created_at')
        else:
            products = Product.objects.none()
        return products
# Till here   

class SingleProductView(LoginRequiredMixin,DetailView):
    model = Product
    template_name = 'userportal/single_product.html'

class UserDetailView(SuccessMessageMixin ,LoginRequiredMixin, DetailView):
    model = User
    template_name = 'adminportal/single_user.html'

class RegisterUser(SuccessMessageMixin, FormView):
    form_class = UserForm
    template_name = 'adminportal/registration.html'
    # success_message = "%(name)s was created successfully"
  

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)   
        user.save()    
        print("user is saving data")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Data is invalid") 
        return super().form_invalid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + " Created Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:login_1')

class UpdateUser(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'adminportal/update.html'
    # success_message = "%(username)s was created successfully"

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)   
        # user.save()    
        print("user is saving data")
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + " Updated Successfully..!!"
  

    def get_success_url(self):
        return reverse('user_urls:user_data')

class DeleteUser(DeleteView):
    model = User
    template_name = 'adminportal/proddel.html'
    context_object_name = 'delete_product'

    def get_success_url(self):
        return reverse('user_urls:user_data')

class AddToCartView(SuccessMessageMixin, LoginRequiredMixin, TemplateView):

    def cart_view(request, *args, **kwargs):

        user = User.objects.filter(username = request.user).first()
        print("user", user)

        order = CartItem.objects.filter(Q(user__username = user))
        print("order", order)

        # cart_item, created = CartItem.objects.get_or_create(user=request.user)[0]
        # print("cart_item", cart_item)

        # items = order.cartitem_set.all()
        # print("items", items)

        context = {'items': order}
        return render(request, 'userportal/cart.html', context=context)


    def add_to_cart(request, *args, **kwargs):

        item_id = request.POST.get('item_id')
        action = request.POST.get('action')

        product, created = Product.objects.get_or_create(id = item_id)
        print("item", product)

        user = User.objects.filter(username = request.user).first()
        print("user", user)

        cart_item, created = CartItem.objects.get_or_create(user = user, product = product)
        print("order", cart_item)

        # cart = CartItem.objects.values()
        # data = list(cart)
        # print("cart", data)
        # data = serializers.serialize('json', cart)

        cart_total = []
        print("Before cart_item_Total price", cart_total)

        if action == "add":
            cart_item.quantity += 1
            cart_total = cart_item.get_cart_total
            # cart_total.append(True)
            print("quntity added by 1: ", cart_total)

            cart_item.save()
        
        elif action == "remove":
            cart_item.quantity -= 1
            cart_total = cart_item.get_cart_total
            # cart_total.append(True)
            print("quntity removed by 1: ", cart_total)
            cart_item.save()
        else:
            print("Something's wrong with the action..!!")

        print(" After cart_item_Total price ", item_id)
        
        cart_item.save()
        print("cart_item", cart_item)
        return JsonResponse({"cart_total" : cart_total, "item_id":item_id}) 


        


    

