from django.urls import path
from .views import *

urlpatterns = [
    path('',home_view, name='home-page'),
    path('about/',about, name='about-page'),
    path('contract/',contract, name='contract-page'),
    path('addproduct/',add_product, name='addproduct-page'),
    path('allproduct/',product, name='allproduct-page'),
    path('register/',register, name='register-page'),
]
