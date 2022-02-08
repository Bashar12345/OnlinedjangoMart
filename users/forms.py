
from django import forms 
from users.db_models import *
#from django.contrib.auth.models import User 
#from django.contrib.auth.forms import UserCreationForm



class user_registration_form(forms.ModelForm):
    #email = forms.EmailField(label='Enter your Email:', max_length=150)
    #password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= Customer
        fields = ('name', 'email', 'password', 'instrument_purchase', 'house_no',
                  'address_line1', 'address_line2', 'telephone', 'zip_code', 'state', 'country')
        labels = {'name': 'Enter your Fullname', 
                  'email': 'Enter your Email Address'}
        widgets = {
               'name': forms.TextInput(attrs={'class': 'form-control-lg'}),
               'email': forms.TextInput(attrs={'class': 'form-control-lg'}), 
               'password': forms.PasswordInput(),
               'instrument_purchase':'',
               'house_no':'',
               'address_line1':'',
               'address_line2':'',
               'telephone':'',
               'zip_code':'',
               'state':'',
               'country':'',
         }
        

    #username= forms.CharField(label='Enter your Username:',max_length=100)
    

