from .models import *
from django import forms 

class productForm(forms.ModelForm):
	product_id = forms.CharField(label='Give a Product code*',min_length =5,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	product_name = forms.CharField(label='Product name*',min_length =5,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

	product_photo = forms.FileField(label='Product image ',widget=forms.FileInput({'class':'form-control'})) 

	product_description = forms.CharField(label='Enter the Present Address', widget=forms.Textarea(attrs={'class': 'form-control','rows':2}))

	class Meta:
		model=product_info
		fields=('product_id','product_name','product_photo','product_description')

class auctioned_product_form(forms.ModelForm):
	minimum_bid_price= forms.DecimalField(label='Minimum bid price*',required=True,widget=forms.NumberInput(attrs={'placeholder':'00.00','class':'form-control'}))

	auction_end_dateTime= forms.DateTimeField(label='Enter the End time of auctioning the product',widget=forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local'}))

	class Meta :
		model= auctioned_product
		fields=  ('minimum_bid_price','auction_end_dateTime')