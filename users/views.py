from django.shortcuts import render
from django.contrib.auth.forms import UserCreationFrom

def register(request):
    form = UserCreationFrom()
    return render(request,'users/register.html',{form:'form'})
