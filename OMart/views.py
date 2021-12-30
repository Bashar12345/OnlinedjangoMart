from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def home(request):
#     return  HttpResponse('<h1> new webapp</h1>')


def home(request):
    return render(request,'OMart/home.html')



def about(request):
    return render(request, 'OMart/about.html', {'title': 'About'})
