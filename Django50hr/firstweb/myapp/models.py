from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,on_delete=models.CASCADE
    )
    photo = models.ImageField(
        upload_to="photoprofile",null=True,
        blank=True,default = 'userprofiledefault.png'
    )
    usertype = models.CharField(max_length=100,default='member')
    cartquan = models.IntegerField(default=0)

    def __str__(self):
        return self.user.first_name

class allProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    detail = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=200, null=True, blank=True)
    instock = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products", null=True, blank=True)
    unit = models.CharField(max_length=200,default="-")
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField()
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

