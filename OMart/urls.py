
from unicodedata import name
from django.urls import path, include
from . import views
from users import views as user_views


urlpatterns = [
    path('', views.home, name='Omart-home'), #urls path address string 
    path('about/', views.about, name='Omart-about'),
    path('users/', user_views.register, name='Omart-register'),
]
