from django.shortcuts import render
from rest_framework import generics
from .models import Productos
from .serializers import ProductoSerializer

# Create your views here.
class ProductoView(generics.ListCreateAPIView):
    queryset=Productos.objects.all()
    # queryset=Productos.objects.filter()
    serializer_class=ProductoSerializer