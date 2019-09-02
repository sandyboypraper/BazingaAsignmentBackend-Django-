from rest_framework import serializers
from .models import orders

class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = orders
        fields = ('id' , 'itemname' , 'quantity' , 'price' , 'customername' , 'contact')
