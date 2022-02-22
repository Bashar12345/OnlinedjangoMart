from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from products.models import product_info, auctioned_product

# Create your views here.


@login_required
def home(request):
    title = "Homepage"
    products = product_info.objects.all()
    return render(request, 'OMart/home.html', {'title': title, 'products': products})


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
