from rest_framework import serializers 
from Productapp.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','Name','Price','Specification','Brand','Rating']