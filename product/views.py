from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
