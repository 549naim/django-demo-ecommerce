from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profilePicture=models.ImageField(upload_to='profilePicture',blank=True)
    addresses=models.TextField(blank=True)
    phoneNumber=models.CharField(max_length=20,blank=True)