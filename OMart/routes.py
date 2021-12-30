from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Omart-home'),
    path('about/', views.about, name='Omart-about'),
]

