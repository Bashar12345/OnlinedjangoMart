from django.db import models
from accounts.models import User
from datetime import datetime,timedelta

# Create your models here.


class product_info(models.Model):
    product_id= models.CharField(primary_key=True,max_length=200)
    product_name = models.CharField(max_length=100,null=False)
    product_description = models.TextField(max_length=2000)
    product_photo = models.ImageField(upload_to='product_img')
    # ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
   
    @classmethod
    def create(cls, product_id,product_name,product_description,product_photo):
        product_info = cls(product_id=product_id,product_name=product_name,product_description=product_description)
        # do something with the book
        return product_info

    def __str__(self):
        #return f'{self.user.email} Profile'
        return f'{self.product_name} '#({self.product_description})'




class auctioned_product(models.Model):
    product = models.OneToOneField(product_info, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    minimum_bid_price = models.DecimalField(default=00.00 , max_digits=8,decimal_places=2,auto_created=True)
    auction_end_dateTime = models.DateTimeField(default=lambda: datetime.now()+timedelta(days=7)) 

    

    def __str__(self):
        #return f'{self.user.email} Profile'
        return f'{self.product.product_id} price: {self.minimum_bid_price}tk    time_left: {self.auction_end_dateTime}'

class user_bidding(models.Model):
    bid_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #current user ashe nahh
    product = models.ForeignKey(auctioned_product, on_delete=models.CASCADE)
    final_bid= models.IntegerField()
    
    # @classmethod
    # def create(cls, bid_id,product,final_bid):
    #     user_bidding = cls(bid_id=bid_id,product=product,final_bid=final_bids)
    #     # do something with the book
    #     return user_bidding

    def __str__(self):
        #return f'{self.user.email} Profile'
        return f'{self.user.email} bidded on {self.product.product.product_id}- last_bided: {self.final_bid}'





# class BookAdmin(admin.ModelAdmin):
#     list_display= ('title', 'author', 'description', 'publicationyear')


# #admin.site.register(Book, BookAdmin)