from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from product.views import allproduct 

def homepage(request):
    if request.user.is_authenticated:
        return redirect(allproduct)
    else:    
        return render(request,"homepage.html")
      


def signup(request):
    if request.user.is_authenticated:
        return redirect(allproduct)
    if request.method == "POST":
        username = request.POST.get('username') 
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password") 
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists")
            elif User.objects.filter(email=email).exists():
                return HttpResponse("Email already exists")
            else:
                try:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                    user.save()
                    return redirect(signin)
                except:
                    return HttpResponse(" something missing .. please try again")
        else:
            return HttpResponse("password didn't match") 
    else:    
        return render(request, "signuppage.html")    

def signin(request):
    if request.user.is_authenticated:
        return redirect(allproduct)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(allproduct)
        else:
            return HttpResponse("invalid username or password")    
    return render(request, "loginpage.html")

def signout(request):
    logout(request)
    return redirect(homepage)

def userprofile(request):
    if request.user.is_authenticated:
        return render(request,'userprofile/viewprofile.html',{'name':request.user.get_full_name(),'email':request.user.email,'username':request.user.username})
    else:
        return redirect(signin) 

def editinfo(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            user=request.user
            if firstname is not None or firstname !="":
                user.first_name = firstname
            if lastname is not None or lastname !="":
                user.last_name = lastname
            if email is not None and email !="":
                # if User.objects.filter(email=email).exists(): 
                #     return HttpResponse("Email already exists")
                # else:
                user.email = email    
            user.save()
            return redirect(allproduct)
        else:
            return render(request,'userprofile/editinfo.html',{'firstname':request.user.first_name,'lastname':request.user.last_name,'email':request.user.email})
    else:
        return redirect(userprofile)        

def changepass(request):   
    if request.user.is_authenticated:
        if request.method == 'POST':
            user=request.user
            oldpassword=request.POST.get('oldpassword')
            newpassword=request.POST.get('newpassword')
            newpassword2 = request.POST.get('newpassword2')
            if user.check_password(oldpassword):
                if newpassword == newpassword2:
                    user.set_password(newpassword)
                    user.save()
                    return redirect(signin)
                else:
                    return HttpResponse("password do not match")
            else:
                return render(request, 'userprofile/changepass.html')
        else:
            return render(request, 'userprofile/changepass.html')        
    else:
        return redirect('home')        