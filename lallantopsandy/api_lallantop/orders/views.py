from django.shortcuts import render
from rest_framework import viewsets
from .models import orders
from .serializers import OrderSerializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
import json

# Create your views here.
class orderView(viewsets.ModelViewSet):
    queryset = orders.objects.all()
    serializer_class = OrderSerializers



@method_decorator(csrf_exempt, name='dispatch')
class createOrders(View):
    def post(self , request , *args , **kwargs):
        data = json.loads(request.body)
        print("heyy")
        print(json.dumps(data , indent=4, sort_keys=True))
        print("hthth")
        listitem = data["line_items"]

        customername = data["customer"]["first_name"] + data["customer"]["last_name"]
        email = data["customer"]["email"]
        contact = ""
        if email:
            contact = email
        else:
            contact = data["customer"]["phone"]

        for temp in range(len(listitem)):
            itemname = listitem[temp]["name"]
            quantity = listitem[temp]["quantity"]
            price = listitem[temp]["price"]
            o = orders(customername = customername , contact = contact ,itemname = itemname, quantity = quantity , price = price)
            o.save()

        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class editOrder(View):
    def post(self , request , *args , **kwargs):
        data = json.loads(request.body)
        print("heyy")
        print(json.dumps(data , indent=4, sort_keys=True))
        print("hthth")

        orderid = data["id"]
        ordercontact = data["contact"]

        o = orders.objects.get(id = orderid)
        o.contact = ordercontact

        o.save()

        return HttpResponse()

