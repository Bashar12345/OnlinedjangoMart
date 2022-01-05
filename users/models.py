from django.db import models
from django.utils import timezone

# Create your models here.


class user(models.Model):
    usernauser_email = models.CharField(max_length=200)
    user_name = models.TextField()
    date_of_sign_up = models.DateTimeField(default=timezone.now)
