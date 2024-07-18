from django.shortcuts import render
from .models import ProductMod


def IndexPage(request):
    obj = ProductMod.objects.all()
    return render(request,'goods/index.html',{'obj':obj})