from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.homepage, name='homepage'),
    path('login/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    # path('mainhome/', views.mainhome, name='mainhome'),
    path('logout/', views.signout, name='logout'),
    path('viewprofile/', views.userprofile, name='viewprofile'),
    path('editinfo/', views.editinfo, name='editinfo'),
    path('changepass/', views.changepass, name='changepass'),


]