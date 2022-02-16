# from turtle import title
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib import messages
#from matplotlib.pyplot import title
from .forms import user_registration_form

def register(request):
    title='SignUp'

    if request.method == 'POST':
      form = user_registration_form(request.POST)
      if form.is_valid():
            print(form.cleaned_data)
            form.save()
            name =form.cleaned_data.get('name') # username database e ase na 
          # need fixing
            print(name)
            # email = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password')
            # confrim_password = form.cleaned_data.get('confrim_password')
            # instrument_purchase = form.cleaned_data.get('instrument_purchase')
            # house_no = form.cleaned_data.get('house_no')
            # address_line1 = form.cleaned_data.get('address_line1')
            # address_line2 = form.cleaned_data.get('address_line2')
            # telephone = form.cleaned_data.get('telephone')
            # zip_code = form.cleaned_data.get('zip_code')
            # state = form.cleaned_data.get('state')
            # country = form.cleaned_data.get('country')
    
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # print(username)
            # print(email)
            messages.success(request,f'Account created for {name}!')
            return redirect('Omart-home')
    else:
      form = user_registration_form()

    return render(request,'users/register.html', {'form':form, 'title':title})



# def login(request):
#     title= 'login'
     
#     if request.method == 'POST':
      
#             messages.success(request,f'Account created for {username}!')
#             return redirect('Omart-home')
#     else:
#       form = 

#     return render(request,'users/login.html', {'form':form, 'title':title})
