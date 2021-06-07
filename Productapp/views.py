from django.shortcuts import render,HttpResponse,redirect
from .models import Product,bigImage,smallImage,mediumImage,Cart,Store,Wallet
from Accounts.models import CustomUser
from django.http import JsonResponse
from django.core import serializers
import json


# Create your views here.


def Mobileview(request,order=None):
    all_products=Product.objects.filter(category='Mobile Phones')
    search_term='Search'
    if order:
        if order==1:
            all_products=all_products.order_by('Price')
        elif order==2:
            all_products=all_products.order_by('-Price')
        elif order==3:
            all_products=all_products.order_by('-Rating')
        elif order==4:
            all_products=all_products.order_by('Rating')
    image_list=[]
    for product in all_products:
        Image=mediumImage.objects.filter(product=product).first()
        image_list.append(Image)
    return render(request,'products.html',{'all_products':zip(all_products,image_list),'search_term': search_term,'url':'Mobiles'})




def ACview(request,order=None):
    all_products=Product.objects.filter(category='ACs')
    search_term='Search'
    if order:
        if order==1:
            all_products=all_products.order_by('Price')
        elif order==2:
            all_products=all_products.order_by('-Price')
        elif order==3:
            all_products=all_products.order_by('-Rating')
        elif order==4:
            all_products=all_products.order_by('Rating')
    image_list=[]
    for product in all_products:
        Image=mediumImage.objects.filter(product=product).first()
        image_list.append(Image)
    return render(request,'products2.html',{'all_products':zip(all_products,image_list),'search_term': search_term,'url':'ACs'})


def Laptopview(request,order=None):
    all_products=Product.objects.filter(category='Laptops')
    search_term='Search'
    if order:
        if order==1:
            all_products=all_products.order_by('Price')
        elif order==2:
            all_products=all_products.order_by('-Price')
        elif order==3:
            all_products=all_products.order_by('-Rating')
        elif order==4:
            all_products=all_products.order_by('Rating')
    image_list=[]
    for product in all_products:
        Image=mediumImage.objects.filter(product=product).first()
        image_list.append(Image)
    return render(request,'products.html',{'all_products':zip(all_products,image_list),'search_term': search_term,'url':'Laptops'})


def Tabletview(request,order=None):
    all_products=Product.objects.filter(category='Tablets')
    search_term='Search'
    if order:
        if order==1:
            all_products=all_products.order_by('Price')
        elif order==2:
            all_products=all_products.order_by('-Price')
        elif order==3:
            all_products=all_products.order_by('-Rating')
        elif order==4:
            all_products=all_products.order_by('Rating')
    image_list=[]
    for product in all_products:
        Image=mediumImage.objects.filter(product=product).first()
        image_list.append(Image)
    return render(request,'products.html',{'all_products':zip(all_products,image_list),'search_term': search_term,'url':'Tablets'})

def TVview(request,order=None):
    all_products=Product.objects.filter(category='TVs')
    search_term='Search'
    if order:
        if order==1:
            all_products=all_products.order_by('Price')
        elif order==2:
            all_products=all_products.order_by('-Price')
        elif order==3:
            all_products=all_products.order_by('-Rating')
        elif order==4:
            all_products=all_products.order_by('Rating')
    image_list=[]
    for product in all_products:
        Image=mediumImage.objects.filter(product=product).first()
        image_list.append(Image)
    return render(request,'products2.html',{'all_products':zip(all_products,image_list),'search_term': search_term,'url':'TVs'})

def Cameraview(request,order=None):
    all_products=Product.objects.filter(category='Cameras')
    search_term='Search'
    if order:
        if order==1:
            all_products=all_products.order_by('Price')
        elif order==2:
            all_products=all_products.order_by('-Price')
        elif order==3:
            all_products=all_products.order_by('-Rating')
        elif order==4:
            all_products=all_products.order_by('Rating')
    image_list=[]
    for product in all_products:
        Image=mediumImage.objects.filter(product=product).first()
        image_list.append(Image)
    return render(request,'products2.html',{'all_products':zip(all_products,image_list),'search_term': search_term,'url':'Cameras'})

def MobileAccessoriesview(request,order=None):
    all_products=Product.objects.filter(category='Headphones And Headsets').union(Product.objects.filter(category='Memory Cards'))
    search_term='Search'
    if order:
        if order==1:
            all_products=all_products.order_by('Price')
        elif order==2:
            all_products=all_products.order_by('-Price')
        elif order==3:
            all_products=all_products.order_by('-Rating')
        elif order==4:
            all_products=all_products.order_by('Rating')
    image_list=[]
    for product in all_products:
        Image=mediumImage.objects.filter(product=product).first()
        image_list.append(Image)
    return render(request,'products1.html',{'all_products':zip(all_products,image_list),'search_term': search_term,'url':'mobile-accesories'})

def ComputerAccessoriesview(request,order=None):
    all_products=Product.objects.filter(category='Pen Drives').union(Product.objects.filter(category='Keyboards'))
    search_term='Search'
    if order:
        if order==1:
            all_products=all_products.order_by('Price')
        elif order==2:
            all_products=all_products.order_by('-Price')
        elif order==3:
            all_products=all_products.order_by('-Rating')
        elif order==4:
            all_products=all_products.order_by('Rating')
    image_list=[]
    for product in all_products:
        Image=mediumImage.objects.filter(product=product).first()
        image_list.append(Image)
    return render(request,'products1.html',{'all_products':zip(all_products,image_list),'search_term': search_term,'url':'computer-accesories'})

def WearableAccessoriesview(request,order=None):
    all_products=Product.objects.filter(category='Smartwatches').union(Product.objects.filter(category='Fitness Bands'))
    search_term='Search'
    if order:
        if order==1:
            all_products=all_products.order_by('Price')
        elif order==2:
            all_products=all_products.order_by('-Price')
        elif order==3:
            all_products=all_products.order_by('-Rating')
        elif order==4:
            all_products=all_products.order_by('Rating')
    image_list=[]
    for product in all_products:
        Image=mediumImage.objects.filter(product=product).first()
        image_list.append(Image)
    return render(request,'products1.html',{'all_products':zip(all_products,image_list),'search_term': search_term,'url':'wearable-accesories'})

def detailview(request,pk):
    product=Product.objects.get(id=pk)
    store=Store.objects.filter(product=product)
    specification=json.loads(product.Details)
    BigImage=bigImage.objects.filter(product=product)
    MediumImage=mediumImage.objects.filter(product=product)
    SmallImage=smallImage.objects.filter(product=product)

    related=Product.objects.filter(category=product.category)
    related_images=[]
    r_list=[]
    cnt=0
    for p in related:
        if p.id!=product.id and cnt<4:
            r_list.append(p)    
            related_images.append(mediumImage.objects.filter(product=p).first())
            cnt+=1
    context={"product": product, "stores": store,'BigImage':BigImage,"MediumImage":MediumImage,"SmallImage":SmallImage,'Images':zip(BigImage,SmallImage),'spec':specification,
    'related':zip(r_list,related_images)}
    return render(request=request, template_name="single.html",context=context)


def cartview(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            user_id=request.POST.get('user')
            user=CustomUser.objects.get(id=user_id)
            product_id=request.POST.get('product_id')
            product=Product.objects.get(id=product_id)
            cart,status=Cart.objects.get_or_create(user=user)
            cart.save()
            cart.product.add(product)
            cart.save()
            x=len(cart.product.all())
            return HttpResponse(x)
        else:
            return HttpResponse(0)


def cartremoveview(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            user_id=request.POST.get('user')
            user=CustomUser.objects.get(id=user_id)
            product_id=request.POST.get('product_id')
            product=Product.objects.get(id=product_id)
            cart=Cart.objects.get(user=user)
            cart.product.remove(product)
            cart.save()
            print(cart.product.all())
            return HttpResponse(len(cart.product.all()))
        else:
            return HttpResponse(0)

def searchview(request):
    if request.method =='POST':
        search_term=request.POST.get('item_name')
    else:
        search_term=""
    articles = Product.objects.all().filter(Name__icontains=search_term) 
    newlen=min(len(articles),10)  
    mydict={}
    for article in articles[:newlen]:
        mydict[article.Name]="/product/"+str(article.pk)
    return JsonResponse(mydict)

def searchresultview(request):
    if request.method =='POST':
        search_term = request.POST.get('Search')
        if search_term!='':
            items= Product.objects.all().filter(Name__icontains=search_term).union(Product.objects.all().filter(category__icontains=search_term))
            if items:
                imglist=[]
                productlist=[]
                for product in items:
                    img=mediumImage.objects.filter(product=product).first()
                    imglist.append(img)
                    productlist.append(product)
                context={'products':zip(productlist,imglist),'total':len(productlist),'no_result':False}
            else:
                context={'no_result':True}
            return render(request,'search_results.html',context=context)
        else:
            return render(request,'search_results.html',context={})
    else:
        return render(request,'search_results.html',context={'no_result':True})



def dashboardview(request):
    user=request.user
    if user.is_authenticated:
        cart,status=Cart.objects.get_or_create(user=user)
        wallet,status=Wallet.objects.get_or_create(user=user)
        imglist=[]
        productlist=[]
        storelist=[]
        for product in cart.product.all():
            img=mediumImage.objects.filter(product=product).first()
            store=Store.objects.filter(product=product)
            storelist.append(store)
            imglist.append(img)
            productlist.append(product)
        return render(request,'dashboard.html',{'cart':zip(productlist,imglist,storelist),'items':len(productlist),'amount':wallet.get_amount()})
    else:
        return render(request,'dashboard.html',{'message':True})

def get_cart_no(request):
    user=request.user
    if user.is_authenticated:
        cart,status=Cart.objects.get_or_create(user=user)
        return HttpResponse(len(cart.product.all()))
    else:
        return HttpResponse(0)
        
