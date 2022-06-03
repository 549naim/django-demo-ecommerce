from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.allproduct, name='allproduct'),
    path('<int:p_id>/',views.singleproduct,name='singleproduct'),
    path('add_to_cart/<int:p_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:p_id>/',views.remove_from_cart,name='remove_from_cart'),
    path("search/<str:string>/",views.search_view,name='search_view') 

    
]