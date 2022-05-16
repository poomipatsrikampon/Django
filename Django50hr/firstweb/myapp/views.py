
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# import upload FILE
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home_view(request):

    return render(request,'myapp/home.html')


def about(request):
    return render(request,'myapp/about.html')


def contract(request):
    return render(request,'myapp/contract.html')


def add_product(request):
    
    if request.method =='POST' and request.FILES['imageupload']:

        data = request.POST.copy()
        name = data.get('name')
        price = data.get('price')
        image_url = data.get('imageurl')
        detail = data.get('detail')
        quantity = data.get('quantity')
        unit = data.get('unit')

        new = allProduct()
        new.name = name
        new.price = price
        new.image_url =image_url
        new.detail = detail
        new.quantity = quantity
        new.unit = unit

        #upload image------------
        file_image = request.FILES['imageupload']
        file_image_name = request.FILES['imageupload'].name.replace(' ','')
        fs = FileSystemStorage()
        filename =fs.save(file_image_name,file_image)
        upload_file_url = fs.url(filename)

        new.image = upload_file_url[6:]
        #------------------------
        new.save()

    
    return render(request,'myapp/addproduct.html')


def product(request):

    product = allProduct.objects.all().order_by('id').reverse()
    context = {
        'product':product
    }

    
    return render(request,'myapp/allproduct.html',context)

