
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RecommendationGuid.settings")
import django
django.setup()

from Productapp.models import Product,Store,bigImage,mediumImage,smallImage
from bs4 import BeautifulSoup
import html5lib
import sys
import requests
from collections import OrderedDict 
from json import dumps,loads


sys.stdin=open("input.txt","r")
# sys.stdout=open("output.txt","w",encoding="utf-8")




class store:
    def __init__(self,logo,price,link,store_name):
        self.logo=logo
        self.price=price
        self.link=link
        self.store_name=store_name
    
    def __str__(self):
        return self.store_name

    def show_store(self):
        print("Name : ",self.store_name)
        print("Price : ",self.price)
        print("Logo : ",self.logo)
        print("Link : ",self.link)


    
def make_price(s):
    if '₹' in s:
        s=s.replace('₹','')
    if ',' in s:
        s=s.replace(',','')
    if u'\xa0Lacs' in s:
        s=s.replace(u'\xa0Lacs','')
        s=float(s)*100000
    else:
        s=float(s)
    return str(round(s,1))



def Name_and_Brand(soup):
    heading=soup.find('div',attrs={"id":"page-heading"})
    Name=heading.find('h1').text 
    Brand=heading.find('a').text 
    return [Name,Brand]


def Current_price(soup):
    Price=soup.find('span',attrs={"class":"price"})
    return make_price(str(Price.text))


def Rating(soup):
    maintag=soup.find('div',attrs={"id":"product-info"})
    tag=soup.find('div',attrs={"id":"product-review"})
    span=tag.find('span',attrs={"class":"rating-value rank-1-f"})
    rating=str(span.text)
    rating=rating.replace('/ 10','')    
    return float(rating)/2




def Image_links(soup):
    image_div=soup.find('div',attrs={"class":"small-imgs"})
    image_list=[]
    if image_div:
        image_tags=image_div.find_all('a')
        for images in image_tags:
            images=str(images)
            image1=images[images.find('http'):images.find('jpg')+3]
            image2=image1.replace('w1200-h1200','w240-h290')
            image3=image1.replace('w1200-h1200','w50-h60')
            image_list.append((image1,image2,image3))
    else:
        image_div=soup.find('div',attrs={"class":"large-img"})
        image_tags=image_div.find('img')
        images=str(image_tags)
        image2=images[images.find('http'):images.find('jpg')+3]
        image1=image2.replace('w240-h290','w1200-h1200')
        image3=image2.replace('w240-h290','w50-h60')
        image_list=[(image1,image2,image3)]
    return image_list




def Specifications(soup):
    features_div=soup.find('div',attrs={"class":"product-features"})
    features=features_div.find_all('span')
    feature_list=''
    for feature in features:
        feature_list+=str(feature.text)+"\n" 
    return feature_list

def Get_Category(soup):
    main=soup.find('div',attrs={'id':'breadcrumbs'})
    sub=main.find('div',attrs={'class':'wrapper'})
    category=sub.find_all('a')[1].text
    return category
    

def Full_Specifications(soup):
    full_spec_div=soup.find('div',attrs={"class":"spec-box","id":"full-specs"})
    left_table=full_spec_div.find('table',attrs={"class":"specs-table left"})
    right_table=full_spec_div.find('table',attrs={"class":"specs-table right"})
    main_dict=OrderedDict()
    def Table_fill(table,main_dict):
        table_data=table.find_all('tr')
        for data_row in table_data:
            if bool(data_row.attrs) and data_row.attrs['class']==['heading']:
                current_head=data_row.text
                sub_dict=OrderedDict()
            elif bool(data_row.attrs) and data_row.attrs['class']==['gap']:
                main_dict[current_head]=sub_dict
            else:
                data_cols=data_row.find_all('td')
                for col in data_cols:
                    if bool(col.attrs) and col.attrs['class']==['bold']:
                        item=col.text
                    else:
                        value=col.text
                        sub_dict[item]=value

    Table_fill(left_table,main_dict)
    Table_fill(right_table,main_dict)
    my_json=dumps(main_dict,indent=4)
    return my_json

def Get_stores(soup):
    price_comparison=soup.find('div',attrs={"id":"compare-prices"})
    table=price_comparison.find('tbody')
    table_element=table.find_all('tr',recursive=False)
    storelist=[]
    for element in table_element:
        if bool(element.attrs) and element['class']!=['offer']:
            table_data=element.find_all('td')
            logo_td=table_data[0] 
            logo=logo_td.find('img')['src']
            store_name=logo_td.find('img')['alt']
            link=table_data[4].a['href']
            all_prices=table_data[3].find('div',attrs={'class':'variant-div'})
            if all_prices:
                all_prices.decompose()
            price=table_data[3].text
            new_store=store(logo=logo,price=price,link=link,store_name=store_name)
            storelist.append(new_store)
    return storelist


def update_product():
    sys.stdin = open("output.txt", "r")
    try:
        while True:
            P={}
            url=input()
            if url=="":
                print('updation done')
                break
            r=requests.get(url)
            soup=BeautifulSoup(r.content,"html5lib")
            try:
                P['Name']=Name_and_Brand(soup)
                P['Price']=Current_price(soup)
                try:
                    P['Store']=Get_stores(soup)
                except:
                    P['Store']=[]
            except:
                continue
            try:
                old=Product.objects.get(Name=P['Name'][0])
                if old.Price==P['Price']:
                    print(P['Name'][0],old.Price,P['Price'])
                else:
                    old.Price=P['Price']
                    old.save()
                if P['Store']:
                    Store.objects.filter(product=old).delete()
                    for store in P['Store']:
                        newstore=Store(logo=store.logo,price=store.price,link=store.link,store_name=store.store_name,product=old)
                        newstore.save()
                    print(old.Name+" updated ")
            except Product.DoesNotExist:
                continue
    except EOFError:
        print("Successfully Traversed")
    except :
        print("Space Error")








def Execute():
    try:
        while True:
            P={}
            url=input()
            if url=="":
                break
            r=requests.get(url)
            soup=BeautifulSoup(r.content,"html5lib")
            try:
                P['Name']=Name_and_Brand(soup)
                P['Price']=Current_price(soup)
                P['Highlights']=Specifications(soup)
                P['Image']=Image_links(soup)
                P['Details']=Full_Specifications(soup)
                P['Category']=Get_Category(soup)
                P['Rating']=Rating(soup)
                try:
                    P['Store']=Get_stores(soup)
                except:
                    P['Store']=[]
            except:
                continue
            try:
                if Product.objects.get(Name=P['Name'][0]):
                    print(P['Name'][0]+" already present")
                else:
                    newProduct=Product(Name=P['Name'][0],Price=P['Price'],Specification=P['Highlights'],Details=P['Details'],category=P['Category'],Brand=P['Name'][1],Rating=P['Rating'])
                    newProduct.save()
                    for store in P['Store']:
                        newstore=Store(logo=store.logo,price=store.price,link=store.link,store_name=store.store_name,product=newProduct)
                        newstore.save()
                    for images in P['Image']:
                        image1=bigImage(image=images[0],product=newProduct)
                        image1.save()
                        image2=bigImage(image=images[1],product=newProduct)
                        image2.save()
                        image3=bigImage(image=images[2],product=newProduct)
                        image3.save()
                    print(P['Name'][0]+" added")
            except:
                newProduct=Product(Name=P['Name'][0],Price=P['Price'],Specification=P['Highlights'],Details=P['Details'],category=P['Category'],Brand=P['Name'][1],Rating=P['Rating'])
                newProduct.save()
                for store in P['Store']:
                        newstore=Store(logo=store.logo,price=store.price,link=store.link,store_name=store.store_name,product=newProduct)
                        newstore.save()
                for images in P['Image']:
                        image1=bigImage(image=images[0],product=newProduct)
                        image1.save()
                        image2=mediumImage(image=images[1],product=newProduct)
                        image2.save()
                        image3=smallImage(image=images[2],product=newProduct)
                        image3.save()
                print(P['Name'][0]+" added")
    except EOFError:
        print("Successfully executed !!")

Execute()

# import time

# while True:
#     update_product()
#     time.sleep(30)
