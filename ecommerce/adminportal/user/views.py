from django.db.models.query_utils import Q
from django.http import JsonResponse
from django.views import View
from django.urls import reverse, reverse_lazy 
from django.views.generic import ListView
from generic.views import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import *
from adminportal.product.models import *

# Create BaseView For the below classes

class HomeView(ListView):

    context_object_name = 'items'
    model = Product
    # model = models.ProductImage
    template_name = 'userportal/index.html' 

class AdminHomeView(PermissionRequiredMixin, BaseListView):

    raise_exception = False
    permission_required = 'is_staff'
    redirect_field_name = 'next'
    model = Product
    # model = models.ProductImage
    context_object_name = 'items'
    template_name = 'adminportal/index.html'

    def dispatch(self, request, *args, **kwargs):
            if not self.request.user.is_staff:
                # path_redirect = request.get_full_path().split('?next=',1)
                # print("------------------->>>", path_redirect)
                # if '?next=' in request.get_full_path():# Redirecting After Login 
                #     print("<------- inside if")
                #     # return redirect(path_redirect)
                #     return redirect_to_login(self.path_redirect, self.get_login_url(), self.get_redirect_field_name()) 
                # else:
                return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name()) 

            if not self.has_permission():
                return redirect('/login/')
                
            return super(AdminHomeView, self).dispatch(request, *args ,**kwargs)

class AdminUserView(BaseListView):

    model = User 
    template_name = 'adminportal/user.html'
    context_object_name = 'user_data'   
        

class UserDetailView(BaseDetailView):

    model = User
    template_name = 'adminportal/single_user.html'

class AdminLoginView(LoginView):

    template_name='adminportal/login.html'

    def get_success_url(self):
        return reverse_lazy('user_urls:admin_customized')

class RegisterAdminUserView(BaseRegisterView):

    template_name = 'adminportal/registration.html'
    # success_message = "%(name)s was created successfully"
  
    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True   
        user.save()    
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('user_urls:login_1')


class UpdateUser(BaseUpdateView):

    model = User
    form_class = AdminForm
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

class DeleteUser(BaseDeleteView):

    model = User
    template_name = 'userportal/proddel.html'
    context_object_name = 'delete_product'

    def get_success_message(self, cleaned_data):
        return "Deleted Successfully..!!"

    def get_success_url(self):
        return reverse('user_urls:user_data')

class CartListView(BaseListView):

    model = CartItem
    template_name = 'userportal/cart.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_total"] = CartItem(user = self.request.user)
        return context

    def get_queryset(self):
        user = User.objects.filter(username = self.request.user).first()
        print("user", user)
        queryset = CartItem.objects.filter(Q(user__username = user))
        return queryset
    
class AddToCartView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):

        item_id = request.POST.get('item_id')
        action = request.POST.get('action')
        quan = int(request.POST.get('quantity', 1))
        # print("quan", quan)
        try:
            product = Product.objects.get(id = item_id)
        except Exception as e:
            product = None

        user = User.objects.filter(username = request.user).first()
        # print("user", user)

        cart_item, created = CartItem.objects.get_or_create(user = user, product = product)
        # cart_object = CartItem(product = product, user = user)
        # print("cart-object", cart_object)
        # cart_object.delete()
        # print("cart-object", cart_object)

        print("CART_ITEM------->>>>", cart_item)
      
        cart_total = cart_item.get_cart_total
        get_cart_total = cart_item.get_total
        # print("Before cart_item_Total price", cart_item.quantity)

        if action == "add":
            if quan > 1:
                cart_item.quantity = cart_item.quantity + quan
                cart_total = cart_item.get_cart_total
            else:
                cart_item.quantity += 1
                cart_total = cart_item.get_cart_total

            cart_item.save()
        
        elif action == "remove":
            if cart_item.quantity <= 1:
                print("cart_item", cart_item)
                cart_item.delete()
                # cart_item.save()
                # cart_total = cart_item.get_cart_total 
                return JsonResponse({"product_total" : cart_total, "item_id":item_id, "get_cart_total" : get_cart_total}) 
            else:
                cart_item.quantity -= 1
                cart_total = cart_item.get_cart_total
                cart_item.save()

        # print("After cart item quan", cart_item.quantity)
        get_cart_total = cart_item.get_total
        cart_item.save()
        print("cart_item", cart_item)
        return JsonResponse({"product_total" : cart_total, "item_id":item_id, "get_cart_total" : get_cart_total}) 


        


    

