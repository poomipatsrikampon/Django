from django.db import models

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