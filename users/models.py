from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    #email = forms.EmailField(label='Enter your Email:', max_length=150)
    email = models.EmailField(primary_key=True,max_length=150)
    password= models.CharField(max_length=30)


class shipping_address(models.Model):
    #confrim_password = models.CharField(max_length=100)
    #instrument_purchase = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    present_address = models.TextField(max_length=500)
    permanent_address = models.TextField(max_length=500)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.name



class customer_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    joined_date = models.DateTimeField(default=timezone.now) #auto_now_add=True)
    profile_pic = models.BinaryField() #models.FileField() #models.AutoField() #models.ImageField()
    address = models.ForeignKey(shipping_address, on_delete=models.DO_NOTHING, default=False)