
from django.urls import path,include
from . import views
from rest_framework import routers

router =routers.DefaultRouter()
router.register("product_info", views.product_apiView)

urlpatterns = [
   
    path('products/',include(router.urls))
    
]
