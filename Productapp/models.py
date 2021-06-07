from django.db import models
from django.db.models import *
from jsonfield import JSONField
from Accounts.models import CustomUser
# Create your models here.




class Product(models.Model):
    Name = CharField(max_length=100)
    Price = FloatField(max_length=10)
    Specification = CharField(max_length=1000)
    Details = JSONField(default=None)
    category=CharField(max_length=100)
    Brand = CharField(max_length=20,default=None)
    Rating=FloatField(default=0.0)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return 'product/'+str(self.id)



class bigImage(models.Model):
    image=models.CharField(max_length=500)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)


class mediumImage(models.Model):
    image=models.CharField(max_length=500)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)


class smallImage(models.Model):
    image=models.CharField(max_length=500)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)



class Store(models.Model):
    store_name = CharField(max_length=20)
    logo  = CharField(max_length=500)
    link = CharField(max_length=500)
    price= CharField(max_length=10)
    product=ForeignKey(Product,on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField(Product, blank=True)



class Wallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    amount=models.FloatField(default=0)


    def get_amount(self):
        return self.amount
    
    def set_amount(self,amount):
        self.amount=amount