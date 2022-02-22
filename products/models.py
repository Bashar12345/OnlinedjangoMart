from django.db import models
from django.utils import timezone

# Create your models here.

class product_info(models.Model):
    product_id= models.CharField(primary_key=True,max_length=100)
    product_name = models.CharField(max_length=100,null=False)
    product_description = models.CharField(max_length=1200)
    product_photo = models.ImageField(upload_to='product_img')
   

    def __str__(self):
        #return f'{self.user.email} Profile'
        return f'{self.product_name}  and {self.product_description}'

class auctioned_product(models.Model):
    product = models.OneToOneField(product_info, on_delete=models.CASCADE)
    minimum_bid_price = models.DecimalField(default=00.00 , max_digits=8,decimal_places=2)
    auction_end_dateTime = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        #return f'{self.user.email} Profile'
        return f'{self.product.product_name} and {self.auction_end_dateTime} and {self.minimum_bid_price}tk'