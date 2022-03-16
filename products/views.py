from django.utils import timezone
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import auctioned_product_form, productForm, bid_form
from .models import *
from django.db.models import F,Max

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
def product_detail_page(request, product_id):
    title = "product_page"
    current_time = timezone.now()
    # print((product_id))
    #item = product_info.objects(product_id=product_id).first()
    #item= product_info.objects.all()
    #item = product_info.objects.filter(product_id=product_id).first()
    product_address = auctioned_product.objects.get(product_id=product_id)
    #product_address = auctioned_product.objects.filter(product_id=product_id).first()
    bidded_products = user_bidding.objects.filter(product=product_address).order_by('-final_bid')
    end_date =str(product_address.auction_end_dateTime) 
    end_date, ext = end_date.split('+')
    #print(end_date)

    if current_time > product_address.auction_end_dateTime:
       highest_bid = user_bidding.objects.aggregate(Max('final_bid'))['final_bid__max']  # Returns highest
       print(f' name {highest_bid}')
       max_bider_user = user_bidding.objects.filter(final_bid=highest_bid, product=product_address).first()
       
       print(type(max_bider_user))#print(max_bider_user.user.email)
       if max_bider_user==None:
           max_bider_user=0
       print(type(max_bider_user))
       return render(request, 'products/product_view.html', {'title': title, "max_bider_user": max_bider_user, 'product_address': product_address})
    #print(f' item : {item.product_name}')
    
    
    
    if request.method == 'POST':
        form = bid_form(request.POST or None)
        if form.is_valid():
            bided_form = form.save(commit=False)
            current_user = request.user

            user_address = User.objects.filter(email=current_user).first()
            #print(product_address.product.product_id)

            bid = form.cleaned_data.get('final_bid')
            print(bid)

            checkin_bid = user_bidding.objects.filter(
                product=product_address, user=user_address).update(final_bid=bid)
            if checkin_bid:
                messages.success(request, f'{user_address} called for {bid}')
            else:
                bided_form.user = current_user
                bided_form.product = product_address
                bided_form.save()
                messages.success(request, f'latest bid {bid}')

    else:
        form = bid_form()

    return render(request, 'products/product_view.html', {'form': form, 'title': title, 'bidded_products': bidded_products, 'product_address': product_address})


            # bid_receipt = user_bidding.objects.filter(product=product_address,user=user_address).first()
            # print(bid_receipt)

            # if bid_receipt:
            #     bid_receipt.final_bid = bid
            #     bid_receipt.save()

# class product_detail_view(DetailView):
#     model = product_info
#     template_name = 'products/product_view.html'
#     context_object_name="product_address"







def my_posted_items(request):
    title="My posted Items"
    current_user =request.user
    user_address = User.objects.filter(email=current_user).first()  
    
    product_address = auctioned_product.objects.filter(user=user_address)

    return render(request, 'products/my_items.html',{'title':title,"product_address":product_address})




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

