from django.contrib import admin
from django.urls import path, include
from .views import * 
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'user_urls'


urlpatterns = [
    path('',HomeView.as_view(),name='index'),
    path('admin_customized/',AdminHomeView.as_view(),name='admin_customized'),

    path('cart/',views.AddToCartView.add_to_cart,name='add_to_cart'),


    path('user_data/',AdminUserView.as_view(),name='user_data'),
    path('user_update/<int:pk>', UpdateUser.as_view(), name='user_update'),
    path('user_delete/<int:pk>', DeleteUser.as_view(), name='user_delete'),
    path('single_user/<pk>', UserDetailView.as_view(),name='single_user'),

    path('registration/',RegisterUser.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='adminportal/login.html'), name='login_1'),
    path('logout/', LogoutView.as_view(template_name='adminportal/login.html'), name='logout'),

    path('single_product/<pk>', SingleProductView.as_view(),name='single_product'),
    path('search/', SearchView.as_view(), name='search'),

    # path('update_customer/<int:pk> ', CustomerUser.as_view(), name='update_customer'),
    # path('delete_customer/<int:pk> ', DeleteCustomer.as_view(), name='delete_customer'),




]
