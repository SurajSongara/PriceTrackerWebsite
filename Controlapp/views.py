from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from django.core.mail import send_mail

import random
import json
import os


from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.conf import settings

from Accounts.models import CustomUser,Feedback,Subscription
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from Productapp.models import Product,Store,smallImage,mediumImage,bigImage,Cart


def get_product(category,num):
    products=Product.objects.filter(category=category).order_by('-Rating')
    product_list=[]
    image_list=[]
    val=min(len(products),num)
    for product in products[:val]:
        image_list.append(mediumImage.objects.filter(product=product).first())
        product_list.append(product)
    return zip(product_list, image_list)



def productview(request):
    return render(request=request, template_name="products.html")




def home(request):
    context={
        'home':True,
        'Mobiles':get_product('Mobile Phones',8),
        'ACs':get_product('ACs',4),
        'Laptops':get_product('Laptops',4),
        'Tablets':get_product('Tablets',4),
        'wearables':get_product('wearables',4),
        'cameras':get_product('Cameras',4),
    }
    return render(request=request, template_name="index.html",context=context)










def aboutview(request):
    return render(request=request, template_name="about.html")

def mailview(request):
    return render(request=request, template_name="mail.html")

def codesview(request):
    return render(request=request, template_name="codes.html")

def iconsview(request):
    return render(request=request, template_name="icons.html")

def faqview(request):
    return render(request=request, template_name="faq.html")

def starview(request):
    return render(request=request, template_name="stars.html")

def apiview(request):
    return render(request=request, template_name="api.html")








