from django.db import models
from generic.models import BaseField

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
    # image = models.ImageField(upload_to="product/", default = "product/p1.png")
    brand = models.ForeignKey(Brand, related_name="product_brand", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class ProductImage(BaseField):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="product_name", default=1)
    image = models.ImageField(upload_to="product/", default = "product/p1.png")

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url