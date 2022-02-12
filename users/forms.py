
from logging import PlaceHolder
from django import forms 
from users.db_models import *
#from django.contrib.auth.models import User 
#from django.contrib.auth.forms import UserCreationForm



class user_registration_form(forms.ModelForm):
    email1 = forms.EmailField(
        label='Enter your Email  testing :', max_length=150, widget=forms.TextInput(attrs={'class':'form-control-lg'}))
    #password = forms.CharField(widget=forms.PasswordInput) 
    # CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    # field = forms.ChoiceField(choices=CHOICES)
    
    class Meta:
       
        model= Customer
        CHOICES = (('none','Select A country'),('bangladesh ', 'Bangladesh'), ('us', 'US'),)
       
        fields = ('name', 'email', 'password', 'confrim_password', 'house_no', 'address_line1',
                  'address_line2', 'telephone', 'zip_code', 'state', 'country',)  # 'instrument_purchase'
        labels = {'name': 'Enter your Fullname', 
                  #'email': 'Enter your Email Address',
                  'address_line1': 'Present Address','address_line2':'Permanent Address'}
        widgets = {
               #'name': forms.TextInput(attrs={'class': 'form-control-lg'}),
               #'email': forms.TextInput(attrs={'class': 'form-control-lg'}), 
               'password': forms.PasswordInput(),
               'confrim_password' : forms.PasswordInput(),
               #'instrument_purchase':'',
               'house_no':'',
               'address_line1':'',
               'address_line2':'',
               'telephone':'',
               'zip_code':'',
               'state':'',
               'country': forms.Select(attrs={'class': 'form-select'},choices=CHOICES),
         }
        

    #username= forms.CharField(label='Enter your Username:',max_length=100)
    
class user_login_form(forms.ModelForm):
    class Meta:
        model=User
        fields=('email','password')
        
