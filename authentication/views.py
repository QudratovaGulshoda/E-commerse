from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
