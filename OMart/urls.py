
from django.urls import path
from . import views



urlpatterns = [
    #path('', views.home, name='Omart-home'), #urls path address string 
    path('', views.product_list_view.as_view(), name='Omart-home'),

    path('about/', views.about, name='Omart-about'),
    
    
]
