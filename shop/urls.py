from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopPage"),
    path('about/', views.aboutUs, name="AboutUs"),
    path('contact/', views.contactUs, name="ContactUs"),
    path('track/', views.tracking, name="TrackingStatus"),
    path('search/', views.searching, name="Search"),
    path('checkout/', views.checkoutPage, name="Checkout"),
    path('cart/', views.addtoCart, name="Cart"),
    path('products/<int:id>', views.viewProduct, name="ProductView"),
    path('mensware/', views.forMenCategory, name="MenProductView"),
    path('womensware/', views.forWoMenCategory, name="WoMenProductView"),
    path('kidsware/', views.forKidsCategory, name="kidsProductView"),
    
]