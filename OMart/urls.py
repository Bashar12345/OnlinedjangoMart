
from unicodedata import name
from django.urls import path, include
from . import views
from users import views as users_view

urlpatterns = [
    path('', views.home, name='Omart-home'), #urls path address string 
    path('about/', views.about, name='Omart-about'),
    path('register/', users_view.register,name="Omart_register"),

]
