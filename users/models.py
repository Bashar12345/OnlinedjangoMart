from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True,max_length=150)
    password = models.CharField(max_length=100)
    #confrim_password = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    #instrument_purchase = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    present_address = models.TextField(max_length=500)
    permanent_address = models.TextField(max_length=500)
    telephone = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.name


class User(models.Model):
    #email = forms.EmailField(label='Enter your Email:', max_length=150)
    email = models.ForeignKey(
        Customers, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)