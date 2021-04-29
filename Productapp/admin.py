from django.contrib import admin
from .models import Product,smallImage,mediumImage,bigImage,Store,Cart

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['Name','Price','Specification','category','Rating']

class StoreAdmin(admin.ModelAdmin):
    list_display=['store_name','price','link','logo','product']



class bigImageAdmin(admin.ModelAdmin):
    list_display=['image','product']


class mediumImageAdmin(admin.ModelAdmin):
    list_display=['image','product']

class smallImageAdmin(admin.ModelAdmin):
    list_display=['image','product']
   
class CartAdmin(admin.ModelAdmin):
    list_display=['user']




admin.site.register(Product,ProductAdmin)

admin.site.register(Store,StoreAdmin)

admin.site.register(bigImage,bigImageAdmin)

admin.site.register(mediumImage,mediumImageAdmin)

admin.site.register(smallImage,smallImageAdmin)

admin.site.register(Cart,CartAdmin)