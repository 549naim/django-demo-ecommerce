 
from django.http import HttpResponse
from django.shortcuts import render,redirect
from numpy import product


from product.models import *
from user.models import *
from Cart.models import *
from Cart.views import *




# from django.contrib.auth.models import User
from .models import *
# Create your views here.
def allproduct(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            string = request.POST.get('search')
            return redirect(search_view,string=string)
        # else:    
        #     return HttpResponse("Enter the name of a product")

        all_product =Product.objects.all()
        return render(request,"allproduct.html",{'all_product':all_product,'username':request.user.username})
    else:
        return render(request,"goproduct.html")   
    
   
def singleproduct(request,p_id):
    if request.user.is_authenticated:
        one_product =Product.objects.get(id=p_id)
        return render(request,"singleproduct.html",{'product':one_product}) 

def add_to_cart(request, p_id):
    user=request.user
    try:
        cart=Cart.objects.get(user=user)
    except:
        cart=Cart.objects.create(user=user)
    product =Product.objects.get(id=p_id)
    cart.product.add(product)
    cart.save()
    return redirect(view_cart,user_id=request.user.id)        

def remove_from_cart(request,p_id):
    user = request.user
    cart = Cart.objects.get(user=user)
    product=Product.objects.get(id=p_id)
    cart.product.remove(product)
    cart.save()
    return redirect(view_cart,user_id=request.user.id)

def search_view(request,string):
    if string is not None and string != "":
        all_product = Product.objects.filter(p_name__contains=string)
    else:
        all_product = Product.objects.all()    
    return render(request,"searchresult.html",{'all_product':all_product})
          