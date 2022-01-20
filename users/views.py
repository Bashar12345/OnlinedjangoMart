from turtle import title
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    title='SignUp'
    form = UserCreationForm()
    return render(request,'users/register.html', {'form':form},{'title':title})
