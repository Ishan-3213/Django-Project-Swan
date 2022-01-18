from os import name
from . import views
from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'product_urls'

urlpatterns = [
    path('product_creation/', ProductCreateView.as_view(), name='product_creation'),
    path('brand/', BrandCreateView.as_view(), name='brand'),
    path('category/', CategoryCreateView.as_view(), name='category'),
    path('update/<int:pk>', UpdateProduct.as_view(), name='update'),
    path('delete/<int:pk>', DeleteProduct.as_view(), name='delete'),

    
]
