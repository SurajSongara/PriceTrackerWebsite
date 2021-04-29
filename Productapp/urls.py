from django.urls import path,re_path
from . import views


urlpatterns = [

    path('product/<int:pk>',views.detailview,name="product_detail"),
    re_path('product/<int:pk>',views.detailview,name="product_detail"),
    path('Mobiles',views.Mobileview,name="Mobiles"),
    path('Mobiles/<int:order>',views.Mobileview,name="Mobiles"),
    path('Laptops',views.Laptopview,name="Laptops"),
    path('Laptops/<int:order>',views.Laptopview,name="Laptops"),
    path('Tablets',views.Tabletview,name="Tablets"),
    path('Tablets/<int:order>',views.Tabletview,name="Tablets"),
    path('TVs',views.TVview,name="TVs"),
    path('TVs/<int:order>',views.TVview,name="TVs"),
    path('Cameras',views.Cameraview,name="Cameras"),
    path('Cameras/<int:order>',views.Cameraview,name="Cameras"),
    path('ACs',views.ACview,name="ACs"),
    path('ACs/<int:order>',views.ACview,name="ACs"),
    path('mobile-accesories',views.MobileAccessoriesview,name="mobile-accesories"),
    path('mobile-accesories/<int:order>',views.MobileAccessoriesview,name="mobile-accesories"),
    path('computer-accesories',views.ComputerAccessoriesview,name="computer-accesories"),
    path('computer-accesories/<int:order>',views.ComputerAccessoriesview,name="computer-accesories"),
    path('wearable-accesories',views.WearableAccessoriesview,name="wearable-accesories"),
    path('wearable-accesories/<int:order>',views.WearableAccessoriesview,name="wearable-accesories"),
    path('cart',views.cartview,name="cart"),
    path('cartremove',views.cartremoveview,name="cartremove"),
    path('cart_number',views.get_cart_no,name="cart_number"),
    path('search',views.searchview,name="search"),
    path('search_results',views.searchresultview,name="search_results"),
    path('dashboard',views.dashboardview,name='dashboard'),
]