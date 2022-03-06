from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import auctioned_product_form, productForm, bid_form
from .models import *

# Create your views here.


#product-insert
@login_required
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

#'Omart-view_product_detail'
@login_required
def product_page(request, product_id):
    title = "product_page"
    gotten=product_id
    # print((product_id))
    #item = product_info.objects(product_id=product_id).first()
    #item= product_info.objects.all()
    item = product_info.objects.filter(product_id=product_id).first()
    #print(f' item : {item.product_name}')
    if request.method == 'POST':
        form = bid_form(request.POST or None)
        if form.is_valid():
            bided_form =form.save(commit=False)
            current_user =request.user
            product_address = auctioned_product.objects.get(product_id=product_id)
            user_address = User.objects.filter(email=current_user).first()  
            #print(product_address.product.product_id)
        
            bid = form.cleaned_data.get('final_bid')
            print(bid)
            # bid_receipt = user_bidding.objects.filter(product=product_address,user=user_address).first()
            # print(bid_receipt)

            # if bid_receipt:
            #     bid_receipt.final_bid = bid
            #     bid_receipt.save()

            checkin_bid = user_bidding.objects.filter(product=product_address,user=user_address).update(final_bid = bid) 
            if checkin_bid:
                messages.success(request,f'{user_address} called for {bid}')
            else:
                bided_form.user = current_user
                bided_form.product = product_address
                bided_form.save()
                messages.success(request, f'latest bid {bid}')
            
    else:
        form = bid_form()

    return render(request, 'products/product_view.html', {'form': form, 'title': title, 'item': item})


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












#print(current_user)
            #print(form.instance.user)
            #form.instance.user = current_user
            
            
            
            #MyModel.objects.filter(pk=some_value).update(field1='some value')
            
            # b = user_bidding.objects.get(bid_id=1)
            # print(b)

    # print(item.product_name)
    #query= request.GET.get(product_id)
    # print(query)
    #product_id= {'product_id' :product_id}

