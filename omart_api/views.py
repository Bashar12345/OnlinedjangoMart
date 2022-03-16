from django.shortcuts import render
from rest_framework import viewsets
from .models import product_info
from .serializers import productSerializer

# Create your views here.

class product_apiView(viewsets.ModelViewSet):
	queryset = product_info.objects.all()
	serializer_class= productSerializer

