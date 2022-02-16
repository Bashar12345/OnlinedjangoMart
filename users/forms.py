
from .models import *
from django import forms 
#from django.core import validators
#from django.core.exceptions import ValidationError
#from django.contrib.auth.models import User 
#from django.contrib.auth.forms import UserCreationForm



class user_register_form(forms.ModelForm):
    email = forms.EmailField(label='Enter your Email Address :', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control-lg'}))
    #'instrument_purchase':'',
    password=forms.PasswordInput()
    confrim_password = forms.PasswordInput()
    class Meta:
        model=User
        fields = ('email', 'password','confirm_password') 


class user_register_profile_form(forms.ModelForm):
    name = forms.CharField(label='Enter your Fullname',min_length =5,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'placeholder':'+880','class':'form-control'}))
    class Meta:
        model=customer_profile
        fields = ('name', 'telephone') #profile_pic,address

class user_register_shipping_form(forms.ModelForm):
    house_no = forms.CharField(label='Enter the current house No: ', widget=forms.TextInput(attrs={'class': 'form-control'}))

    permanent_address = forms.CharField(label='Enter the Permanent Address:',widget=forms.Textarea(attrs={'class': 'form-control-md','rows':3}))

    present_address = forms.CharField(label='Enter the Present Address', widget=forms.Textarea(attrs={'class': 'form-control','rows':3}))
    
    zip_code = forms.IntegerField(max_value=5,min_value=4,label='Enter the postal code of the area',widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=shipping_address
        S_CHOICES = (('dhaka', 'Dhaka'), ('rajshahi', 'Rajshahi'), ('sylhet','Sylhet'),)
        C_CHOICES = (('none','Select A country'),('bangladesh ', 'Bangladesh'), ('us', 'US'),)

        fields = ('house_no','present_address', 'permanent_address', 'zip_code', 'state', 'country',) 
        widgets = {
            'state': forms.Select(attrs={'class': 'form-select'}, choices=S_CHOICES),

            'country': forms.Select(attrs={'class': 'form-select'}, choices=C_CHOICES),

        }
    
    







    #state = forms.ChoiceField(choices=CHOICES),
    # country = forms.Select(attrs={'class': 'form-select'}, choices=CHOICES),
    #password = forms.CharField(widget=forms.PasswordInput)
    # CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    # field = forms.ChoiceField(choices=CHOICES)











        # fields = UserCreationForm.Meta.fields + ('name', 'email', 'password1', 'password2', 'house_no', 'permanent_address','present_address', 'telephone', 'zip_code', 'state', 'country',)  # 'instrument_purchase'



    #username= forms.CharField(label='Enter your Username:',max_length=100)








# class user_registration_form(forms.ModelForm):
#     email1 = forms.EmailField(
#         label='Enter your Email  testing :', max_length=150, widget=forms.TextInput(attrs={'class':'form-control-label form-control-lg'}))
#     #password = forms.CharField(widget=forms.PasswordInput) 
#     # CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
#     # field = forms.ChoiceField(choices=CHOICES)
#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#          raise ValidationError("Email already exists")
#         return email

    
#     class Meta:
       
#         model= Customer
#         CHOICES = (('none','Select A country'),('bangladesh ', 'Bangladesh'), ('us', 'US'),)
       
#         fields = ('name', 'email', 'password', 'confrim_password', 'house_no', 'address_line1',
#                   'address_line2', 'telephone', 'zip_code', 'state', 'country',)  # 'instrument_purchase'
#         labels = {'name': 'Enter your Fullname', 
#                   #'email': 'Enter your Email Address',
#                   'address_line1': 'Present Address','address_line2':'Permanent Address'}
#         widgets = {
#                #'name': forms.TextInput(attrs={'class': 'form-control-lg'}),
#                #'email': forms.TextInput(attrs={'class': 'form-control-lg'}), 
#                'password': forms.PasswordInput(),
#                'confrim_password' : forms.PasswordInput(),
#                #'instrument_purchase':'',
#                'house_no':'',
#                'address_line1':'',
#                'address_line2':'',
#                'telephone':'',
#                'zip_code':'',
#                'state':'',
#                'country': forms.Select(attrs={'class': 'form-select'},choices=CHOICES),
#          }
        

#     #username= forms.CharField(label='Enter your Username:',max_length=100)
    
# class user_login_form(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=('email','password')
        
