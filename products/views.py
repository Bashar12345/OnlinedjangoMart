from django.shortcuts import render

from products.forms import auctioned_product_form, productForm

# Create your views here.
def products_insert_view(request):
	title='Insert product Form'
	if request.method== 'POST':
		product_Form= productForm(request.POST or None)
		product_Form2 = auctioned_product_form(request.POST or None)
		product = product_Form.save() 
		product_Form2.instance.product = product 
		product_Form2.save()
	else:
		product_Form= productForm()
		product_Form2 = auctioned_product_form()
	return render(request,'products/product_insert.html',{'form1':product_Form,'form2':product_Form2,'title':title})

