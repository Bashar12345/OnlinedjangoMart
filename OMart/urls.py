
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='Omart-home'), #urls path address string 
    path('about/', views.about, name='Omart-about'),

]
