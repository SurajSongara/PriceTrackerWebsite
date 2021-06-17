from django.shortcuts import render
from .Serializers import ProductSerializer
from django.http import JsonResponse 

# Create your views here.



from Productapp .models import Product


def product_detail(request):
    products=Product.objects.all()
    serialized_products=ProductSerializer(products,many=True)
    return JsonResponse(serialized_products.data,safe=False)
    


def product(request,pk):
    product=Product.objects.get(id=pk)
    serialized_products=ProductSerializer(product)
    return JsonResponse(serialized_products.data)

def product_category(request,category):
    product=Product.objects.filter(category=category)
    serialized_products=ProductSerializer(product,many=True)
    return JsonResponse(serialized_products.data,safe=False)

