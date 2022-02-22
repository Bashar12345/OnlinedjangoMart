from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    title = "Homepage"
    return render(request, 'OMart/home.html', {'title': title})


def about(request):
    title = "About"
    return render(request, 'OMart/about.html', {'title': title})


# def home(request):
#     title = "Omart-Homepage"
#     return HttpResponse('home.html', {'title': title})

# def home(request):
#     title = "Omart-Homepage"
#     return render(request,'home.html', {'title': title})
