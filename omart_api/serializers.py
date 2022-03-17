from rest_framework import serializers
from .models import product_info,auctioned_product
from accounts.models import User


	

class productSerializer(serializers.ModelSerializer):

	class Meta:
		model=product_info
		#fields=('product_id','product_name','url')
		fields=('product_id','product_name','product_description','product_photo')
		# extra_kwargs = {
        #      'url': {'view_name': 'api:product-detail', 'lookup_field': 'pk'},
        # #     #'users': {'lookup_field': 'email'}
        # }
		

class auctionedSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=auctioned_product
		print(auctioned_product.user)
		fields=('product','minimum_bid_price','auction_end_dateTime')
		# extra_kwargs = {
        #     'url': {'view_name': 'api:user-detail', 'lookup_field': 'user'},
        #     #'users': {'lookup_field': ''}
        # }

class UserSerialize(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User
		fields=('email',)
        