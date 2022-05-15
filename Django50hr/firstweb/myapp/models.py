from django.db import models

class allProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    detail = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name