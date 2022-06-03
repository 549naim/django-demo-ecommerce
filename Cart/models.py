from msilib.schema import Class
from django.db import models
from product.models import Product
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ManyToManyField(Product)
    def get_total_price(self):
        total_price = 0
        for p in self.product.all():
            total_price += p.p_price 
        return total_price 


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    shipping_address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    shipping_city = models.CharField(max_length=100)
    shipping_district = models.CharField(max_length=100)
    shipping_divition = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email= models.CharField(max_length=100)
   
    def __str__(self):
        return self.user.username   
