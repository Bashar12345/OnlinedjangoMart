from django.shortcuts import render
from django.contrib import messages

from .forms import auctioned_product_form, productForm

# Create your views here.


def products_insert_view(request):
    title = 'Insert product Form'
    if request.method == 'POST':
        product_Form = productForm(request.POST)
        product_Form2 = auctioned_product_form(request.POST )
        if product_Form.is_valid() and product_Form2.is_valid():
            product = product_Form.save()
            product_Form2.instance.product = product
            product_Form2.save()
            name = product_Form.cleaned_data.get('product_name')
            messages.success(request, f" Account created for {name}!")
        else:
            messages.warning(request, f" Invalid Product Info!")
    else:
        product_Form = productForm()
        product_Form2 = auctioned_product_form()
    return render(request, 'products/product_insert.html', {'form1': product_Form, 'form2': product_Form2, 'title': title})






#messages.info
#messages.debug
#messages.error