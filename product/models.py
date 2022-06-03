
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    def __str__(self):
        return self.name
class Stock(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name        

class Product(models.Model):
    p_name=models.CharField(max_length=200)
    p_description=models.TextField(blank=True)
    p_price=models.IntegerField()
    p_image=models.ImageField(upload_to='product_image',blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.ForeignKey(Stock,on_delete=models.CASCADE)   
    def __str__(self):
        return self.p_name
