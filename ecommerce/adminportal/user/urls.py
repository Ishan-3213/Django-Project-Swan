from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

app_name = 'user_urls'


urlpatterns = [
    path('',HomeView.as_view(),name='index'),
    path('admin_customized/',AdminHomeView.as_view(),name='admin_customized'),
    path('registration/',RegisterUser.as_view(), name='registration'),
    path('login_1/',LoginView.as_view(), name='login_1'),
    path('logout/',LoginView.user_logout,name='logout'),



]
