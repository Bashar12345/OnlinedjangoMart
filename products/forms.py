from .models import *
from django import forms 

class productForm(forms.ModelForm):
	product_id = forms.CharField(label='Give a Product code*',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

	product_name = forms.CharField(label='Product name*',required=True,widget=forms.TextInput(attrs={'class': 'form-control','type':'text'}))

	product_photo =forms.FileField(label='Product image',widget=forms.FileInput({'class':'form-control'})) 

	product_description = forms.CharField(label='Product Description', widget=forms.Textarea(attrs={'class': 'form-control','rows':4}))

	class Meta:
		model=product_info
		fields=('product_id','product_name','product_photo','product_description')

class auctioned_product_form(forms.ModelForm):
	minimum_bid_price= forms.DecimalField(label='Minimum bid price*',required=True,widget=forms.NumberInput(attrs={'placeholder':'00.00','class':'form-control'}))

	auction_end_dateTime= forms.DateTimeField(label='Enter the End time of auctioning the product',widget=forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local'}))

	class Meta :
		model= auctioned_product
		fields=  ('minimum_bid_price','auction_end_dateTime')

class bid_form(forms.ModelForm):
	
	class Meta:
		model= user_bidding
		fields={'final_bid'}
		widgets={
			'final_bid':forms.NumberInput(attrs={'class':'form-control-sm'})
		}