from django.contrib import admin
from .models import *

# Register your models here.

class user_biddingAdmin(admin.ModelAdmin):
    list_display= ('bid_id', 'user', 'product', 'final_bid')

admin.site.register(user_bidding, user_biddingAdmin)

class product_infoAdmin(admin.ModelAdmin):
    list_display= ('product_id', 'product_name','product_description')

admin.site.register(product_info, product_infoAdmin)

class auctioned_productAdmin(admin.ModelAdmin):
     list_display= ('user', 'product', 'minimum_bid_price', 'auction_end_dateTime')

admin.site.register(auctioned_product, auctioned_productAdmin)

#admin.site.register(user_bidding)