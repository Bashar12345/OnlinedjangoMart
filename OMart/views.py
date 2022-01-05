from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def home(request):
    title="Omart-Homepage"
    return render_to_response('home.html', {'title': title})


def home(request):
    title = "Omart-Homepage"
    return render_to_response('home.html', {'title': title})











    

# def home(request):
#     title = "Omart-Homepage"
#     return HttpResponse('home.html', {'title': title})

# def home(request):
#     title = "Omart-Homepage"
#     return render(request,'home.html', {'title': title})
