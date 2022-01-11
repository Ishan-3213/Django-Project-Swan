from django.contrib import admin
from django.urls import path, include

app_name = 'product_urls'

urlpatterns = [
    path('', admin.site.urls),
]
