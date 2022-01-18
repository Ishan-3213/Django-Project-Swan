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

    path('update_brand/<int:pk>', UpdateBrandView.as_view(), name='update_brand'),
    path('delete_brand/<int:pk>', DeleteBrandView.as_view(), name='delete_brand'),  

    path('update_category/<int:pk>', UpdateCategoryView.as_view(), name='update_category'),
    path('delete_category/<int:pk>', DeleteCategoryView.as_view(), name='delete_category'),

    path('category_list/', CategoryBrandFilter.as_view(), name='category_list'),

    
]
