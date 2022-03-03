from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.http import JsonResponse
from django.contrib import messages

from .forms import auctioned_product_form, productForm
from .models import *

# Create your views here.


def products_insert_view(request):
    title = 'Insert product Form'
    if request.method == 'POST':
        product_Form = productForm(request.POST,request.FILES )
        product_Form2 = auctioned_product_form(request.POST,request.FILES)
        print(product_Form.changed_data)
        if product_Form.is_valid() and product_Form2.is_valid():
            product = product_Form.save()
            product_Form2.instance.product = product
            product_Form2.save()
            name = product_Form.cleaned_data.get('product_name')
            messages.success(request, f"{name}! inserted to database ")
            #return redirect('Omart-home')
        else:
            messages.warning(request, f" Invalid Product Info!")
    else:
        product_Form = productForm()
        product_Form2 = auctioned_product_form()
    return render(request, 'products/product_insert.html', {'form1': product_Form, 'form2': product_Form2, 'title': title})


def product_page(request, product_id):
    title = "product_page"
    #print((product_id))
    #item = product_info.objects(product_id=product_id).first()
    #item= product_info.objects.all()
    item = product_info.objects.filter(product_id=product_id).first()
    print(f' item : {item.product_name}')
    #print(item.product_name)
    #query= request.GET.get(product_id)
    #print(query)
    #product_id= {'product_id' :product_id}
    return render(request, 'products/product_view.html', {'title': title,'item': item,'product_id':product_id})

class postJsonView(View):
    def get(self,*args,**kwargs):
        #last_bid = list(user_bidding.objects.values())
        last_bid = user_bidding.objects.values_list()
        return JsonResponse({'data':last_bid}) #,safe=False})
        

#messages.info
#messages.debug
#messages.error