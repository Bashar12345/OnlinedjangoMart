
from .models import *
from django import forms 
#from django.core import validators
from django.core.exceptions import ValidationError
#from django.contrib.auth.models import User 
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class user_register_form(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    email = forms.EmailField(label='Enter your Email Address* :', max_length=150, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label='Enter Password* :', widget=forms.PasswordInput(attrs={"class":" form-control"}))
    password2 = forms.CharField(label='Confirm Password* :', widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ['email']
    
    # def clean_email(self):
    #     '''
    #     Verify email is available.
    #     '''
    #     email = self.cleaned_data.get('email')
    #     qs = User.objects.filter(email=email)
    #     if qs.exists():
    #         raise forms.ValidationError("email is taken")
    #     return email

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 is not None and password1 != password2:
            self.add_error("password2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(user_register_form,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    # def save(self, commit = True):  
    #     user = User.objects.create_user(  
    #         #self.cleaned_data['username'],  
    #         self.cleaned_data['email'],  
    #         self.cleaned_data['password1']
    #     )  
    #     return user 
    

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'is_active', 'admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]



class user_login_form(forms.Form):
    email = forms.EmailField(label='Email Address :', max_length=150, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    password = forms.CharField(label='Password :', widget=forms.PasswordInput(attrs={"class": "form-control","id":"user-password"}))

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user or email is not registered ")
        return email



class user_register_profile_form(forms.ModelForm):
   
    name = forms.CharField(label='Enter your Fullname*',min_length =5,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

    
    telephone=forms.IntegerField(label='Cellphone/Mobile Number*',required=True,widget=forms.NumberInput(attrs={'placeholder':'+880','class':'form-control'}))

    joined_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'form-control'}))
    class Meta:
        model=customer_profile
        fields = ('name', 'telephone') #profile_pic,address

class user_register_shipping_form(forms.ModelForm):
    house_no = forms.CharField(label='Enter the current house No: ', widget=forms.TextInput(attrs={'class': 'form-control'}))

    permanent_address = forms.CharField(label='Enter the Permanent Address:',widget=forms.Textarea(attrs={'class': 'form-control','rows':2}))

    present_address = forms.CharField(label='Enter the Present Address', widget=forms.Textarea(attrs={'class': 'form-control','rows':2}))
    
    zip_code = forms.IntegerField(max_value=5000,label='Enter the postal code of the area',widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model=shipping_address
        S_CHOICES = (('dhaka', 'Dhaka'), ('rajshahi', 'Rajshahi'), ('sylhet','Sylhet'),)
        C_CHOICES = (('none','Select A country'),('bangladesh ', 'Bangladesh'), ('us', 'US'),)

        fields = ('house_no','present_address', 'permanent_address', 'zip_code', 'state', 'country',) 
        widgets = {
            'state': forms.Select(attrs={'class': 'form-select'}, choices=S_CHOICES),

            'country': forms.Select(attrs={'class': 'form-select'}, choices=C_CHOICES),

        }
    
    #'instrument_purchase':'',







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
        
