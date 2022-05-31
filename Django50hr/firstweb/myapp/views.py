
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# import upload FILE
from django.core.files.storage import FileSystemStorage
# import auth
from django.contrib.auth.models import User
#import for crate auto login
from django.contrib.auth import authenticate, login

# Create your views here. 
def home_view(request):

    product = allProduct.objects.all().order_by('id').reverse()[:3]
    preorder = allProduct.objects.filter(quantity__lte=0)
    context = {
        'product':product,
        'preorder':preorder
    }


    return render(request,'myapp/home.html',context)


def about(request):
    return render(request,'myapp/about.html')


def contract(request):
    return render(request,'myapp/contract.html')


def add_product(request):

    if request.user.profile.usertype != 'admin':
        return redirect('home-page')
    
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


def register(request):

    if request.method =='POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.email = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.set_password(password)
        newuser.save()

        #auto setting profile
        profile =Profile()
        profile.user = User.objects.get(username=email)
        profile.save()

        #auto login
        user = authenticate(username=email, password=password)
        login(request,user)

    return render(request,'myapp/register.html')


def add_to_cart(request,pid):
    username = request.user.username
    user = User.objects.get(username=username)
    check = allProduct.objects.get(id=pid)

    try:
        newcart = Cart.objects.get(user=user, product_id=str(pid))
        newquan = newcart.quantity + 1
        newcart.quantity = newquan
        newcart.total = newcart.price * newquan
        newcart.save()


        count = Cart.objects.filter(user=user)
        count = sum([c.quantity for c in count ])
        updatequan = Profile.objects.get(user=user)
        updatequan.cartquan = count
        updatequan.save()

        return redirect('allproduct-page')

    except:
        newcart = Cart()
        newcart.user = user
        newcart.product_id = pid
        newcart.product_name= check.name
        newcart.price = check.price
        newcart.quantity = 1
        newcart.total = check.price
        calculate = (check.price) * 1
        newcart.total = calculate
        newcart.save()

        count = Cart.objects.filter(user=user)
        count = sum([c.quantity for c in count ])
        updatequan = Profile.objects.get(user=user)
        updatequan.cartquan = count
        updatequan.save()
        
        return redirect('allproduct-page')


def my_cart(request):
    username = request.user.username
    user = User.objects.get(username=username)
    mycart = Cart.objects.filter(user=user)
    context = {'mycart':mycart}
    return render(request,'myapp/mycart.html', context)

