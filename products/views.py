from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.contrib import messages

from .forms import auctioned_product_form, productForm, bid_form
from .models import *

# Create your views here.


def products_insert_view(request):
    title = 'Insert product Form'
    if request.method == 'POST':
        product_Form = productForm(request.POST, request.FILES)
        product_Form2 = auctioned_product_form(request.POST, request.FILES)
        print(product_Form.changed_data)
        if product_Form.is_valid() and product_Form2.is_valid():
            useR = request.user
            product = product_Form.save()
            product_Form2.instance.product = product
            product_Form2.instance.user = useR
            product_Form2.save()
            name = product_Form.cleaned_data.get('product_name')
            messages.success(request, f"{name}! inserted to database ")
            # return redirect('Omart-home')
        else:
            messages.warning(request, f" Invalid Product Info!")
    else:
        product_Form = productForm()
        product_Form2 = auctioned_product_form()
    return render(request, 'products/product_insert.html', {'form1': product_Form, 'form2': product_Form2, 'title': title})


def product_page(request, product_id):
    title = "product_page"
    # print((product_id))
    #item = product_info.objects(product_id=product_id).first()
    #item= product_info.objects.all()
    item = product_info.objects.filter(product_id=product_id).first()
    #print(f' item : {item.product_name}')
    if request.method == 'POST':
        form = bid_form(request.POST or None)
        if form.is_valid():
            bided_form =form.save(commit=False)
            #product_id = auctioned_product.objects.filter(product_id=product_id)
            product = auctioned_product.objects.get(product_id=product_id)
            print(product)
            current_user =request.user
            print(current_user)
            #print(form.instance.user)
            #form.instance.user = current_user
            bided_form.user = current_user
            bided_form.product = product
            bided_form.save()
            bid = form.cleaned_data.get('final_bid')
            print(bid)
            b = user_bidding.objects.get(bid_id=1)
            print(b)
    else:
        form = bid_form()
    # print(item.product_name)
    #query= request.GET.get(product_id)
    # print(query)
    #product_id= {'product_id' :product_id}
    return render(request, 'products/product_view.html', {'form': form, 'title': title, 'item': item, 'product_id': product_id})


def bidding(request):
    return render(request, 'Omart-view_product_detail')


class postJsonData(View):
    def get(self, *args, **kwargs):
        #last_bid = list(user_bidding.objects.values())
        last_bid = user_bidding.objects.values_list()
        return JsonResponse({'data': last_bid})  # ,safe=False})


# messages.info
# messages.debug
# messages.error

# form_data=request.POST.dict() if request.POST.dict() else print('request data ase nai')
#     print(form_data)
#     bid = form_data.get('bid')
#     print(bid)
