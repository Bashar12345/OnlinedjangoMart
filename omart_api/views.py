from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class user_view(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class= UserSerialize
class product_apiView(viewsets.ModelViewSet):
	queryset = product_info.objects.all()
	#context={'localhost': 'request'}
	serializer_class= productSerializer

class auctioned_products_view(viewsets.ModelViewSet):
	queryset= auctioned_product.objects.all()
	serializer_class = auctionedSerializer