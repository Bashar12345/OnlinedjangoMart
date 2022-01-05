from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.



class auction_post(models.Model):
    title = models.CharField(max_length=500)
    product_name =models.CharField(max_length=80)
    product_description =models.TextField()
    product_photo =models.ImageField()
    minimum_bid_price =models.IntegerField()
    auction_deadline = models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
