
from django.urls import path,include
from . import views
from rest_framework import routers

router =routers.DefaultRouter()
router.register("products", views.product_apiView)
router.register('auctioned_product', views.auctioned_products_view)
router.register('user', views.user_view)

urlpatterns = [
    #path('omart/', views.product_list_view.as_view(), name='Omart-api'),
    path('omart/',include(router.urls))
    
]
