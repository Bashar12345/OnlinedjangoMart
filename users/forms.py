from attr import attr, field
from django import forms 
#from django.core import validators
#from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from matplotlib import widgets


class user_registration_form(UserCreationForm):
    
    CHOICES = (('none', 'Select A country'),
               ('bangladesh ', 'Bangladesh'), ('us', 'US'),)
    name = forms.CharField(label='Enter your Fullname',min_length =5,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'})),
    email1 = forms.EmailField(
        label='Enter your Email Address :', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control-label form-control-lg'}))
    #'instrument_purchase':'',
    house_no = forms.CharField(label='Enter the current house No: ', widget=forms.TextInput(attrs={'class': 'form-control'})),
    permanent_address = forms.CharField(label='Enter the Permanent Address:',widget=forms.Textarea(attrs={'class': 'form-control'})),
    present_address = forms.CharField(label='Enter the Present Address', widget=forms.Textarea(attrs={'class': 'form-control'})),
    telephone=forms.IntegerField(max_value=11,required=True,widget=forms.NumberInput(attrs={'placeholder':'+880','class':'form-control'})),
    zip_code = forms.IntegerField(max_value=5,min_value=4,label='Enter the postal code of the area',widget=forms.TextInput(attrs={'class':'form-control'})),

    state = forms.ChoiceField(choices=CHOICES),
    country = forms.Select(attrs={'class': 'form-select'}, choices=CHOICES),
    #password = forms.CharField(widget=forms.PasswordInput)
    # CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    # field = forms.ChoiceField(choices=CHOICES)
   


    class Meta(UserCreationForm.Meta):

        model= User
        CHOICES = (('none','Select A country'),('bangladesh ', 'Bangladesh'), ('us', 'US'),)

        #fields = ("username", "password1", "password2", "house_no",)

        fields = UserCreationForm.Meta.fields + ('name', 'email', 'password1', 'password2', 'house_no', 'permanent_address','present_address', 'telephone', 'zip_code', 'state', 'country',)  # 'instrument_purchase'



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
        
