from django.db import models

class ProductMod(models.Model):
    name = models.CharField(max_length=100)
    des = models.TextField()
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media')