from django.contrib import admin
from .models import auction_post,user

# Register your models here.
admin.site.register(auction_post)
admin.site.register(user)