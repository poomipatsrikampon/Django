
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def home_view(request):

    return render(request,'myapp/home.html')


def about(request):
    return render(request,'myapp/about.html')


def contract(request):
    return render(request,'myapp/contract.html')


def add_product(request):
    
    if request.method =='POST':

        data = request.POST.copy()
        name = data.get('name')
        price = data.get('price')
        image_url = data.get('imageurl')
        detail = data.get('detail')

        new = allProduct()
        new.name = name
        new.price = price
        new.image_url =image_url
        new.detail = detail
        new.save()

    
    return render(request,'myapp/addproduct.html')


def product(request):

    product = allProduct.objects.all()
    context = {
        'product':product
    }
    
    return render(request,'myapp/allproduct.html',context)