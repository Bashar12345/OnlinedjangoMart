from rest_framework import serializers
from .models import product_info

class productSerializer(serializers.ModelSerializer):
	class Meta:
		model=product_info
		fields=('product_id','product_name','product_description')