from django.db import models
from generic.models import BaseField
from adminportal.user.models import *

# Create your models here.
class Brand(BaseField):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Category(BaseField):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Product(BaseField):
    name = models.CharField(max_length=256)
    price = models.FloatField(null=False)
    detail = models.TextField()
    image = models.ImageField(upload_to="image/", default="image/p1.png" )
    brand = models.ForeignKey(Brand, related_name="product_brand", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

CHOICE = (
    ('0','No'),
    ('1', 'Yes')
           )

class CartItem(BaseField):

    user = models.ForeignKey(User, null=True ,on_delete=models.SET_NULL, related_name="cart_user")
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name="cart_product")
    quantity = models.IntegerField(default=0)
    purchased = models.CharField(max_length=5, choices=CHOICE, default=0)

    def __str__(self):
        return f"{self.quantity} of {self.product} for {self.user}"


# class ProductImage(BaseField):
#     product_id = models.ForeignKey(Product, verbose_name='parent_category', related_name='children',on_delete=models.CASCADE, default=0)
#     image = models.ImageField(upload_to="product/", default="product/p1.png" )

#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ''
#         return url
