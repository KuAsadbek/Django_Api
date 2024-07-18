from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from goods.models import ProductMod
from .rest_api import ProducRest
from rest_framework import permissions


class ProductList(ListAPIView):
    queryset = ProductMod.objects.all()
    serializer_class = ProducRest

class ProductCreate(CreateAPIView):
    queryset = ProductMod.objects.all()
    serializer_class = ProducRest

class ProductUpdate(UpdateAPIView):
    queryset = ProductMod.objects.all()
    serializer_class = ProducRest
    permission_classes = [permissions.IsAuthenticated]

class ProductDelete(DestroyAPIView):
    queryset = ProductMod.objects.all()
    serializer_class = ProducRest

class ProductListCreate(ListCreateAPIView):
    queryset = ProductMod.objects.all()
    serializer_class = ProducRest

class ProductCrud(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProductMod.objects.all()
    serializer_class = ProducRest
