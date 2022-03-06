from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
#from django.contrib.auth.decorators import login_required
from products.models import product_info, auctioned_product

# Create your views here.


#@login_required
def home(request):
    title = "Homepage"
    #products = product_info.objects.all()
    products = auctioned_product.objects.order_by('auction_end_dateTime')
    current_time = timezone.now()
    #dead_line =products.auction_end_dateTime - current_time
    return render(request, 'OMart/home.html', {'title': title, 'products': products,"current_time":current_time})


#@login_required
def about(request):
    title = "About"
    #query= request.GET.get(product_id)
    #print(query)
    #product_id= {'product_id' :product_id}
    return render(request, 'OMart/about.html', {'title': title})





# def home(request):
#     title = "Omart-Homepage"
#     return HttpResponse('home.html', {'title': title})

# def home(request):
#     title = "Omart-Homepage"
#     return render(request,'home.html', {'title': title})
