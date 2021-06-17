from django.urls import path
from .views import *


urlpatterns = [
    path('products',product_detail),
    path('products/<int:pk>',product),
    path('products/<str:category>',product_category)
]


