from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    title = "Homepage"
    return render(request, 'OMart/home.html', {'title': title})

@login_required
def about(request):
    title = "About"
    return render(request, 'OMart/about.html', {'title': title})


# def home(request):
#     title = "Omart-Homepage"
#     return HttpResponse('home.html', {'title': title})

# def home(request):
#     title = "Omart-Homepage"
#     return render(request,'home.html', {'title': title})
