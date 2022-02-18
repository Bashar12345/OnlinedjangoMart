# from turtle import title
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib import messages
#from matplotlib.pyplot import title
from .models import User
from .forms import user_register_form,user_register_profile_form

def register(request):
    title='SignUp'

    if request.method == 'POST':
      user_form = user_register_form(request.POST or None)
      user_profile_form = user_register_profile_form(request.POST)
      
      
      if user_form.is_valid() and user_profile_form.is_valid() :
          print(user_form.cleaned_data)
          email =user_profile_form.cleaned_data.get('email')
          print(email)
          if not User.objects.filter(email=email).exists():
            name =user_profile_form.cleaned_data.get('name')
            print(name)
            user = user_form.save()
            user_profile_form.instance.user=user
            user_profile_form.save()
            # username database e ase na 
          # need fixing
            
            
            messages.success(request,f" Account created for {name}!")
            return redirect('Omart-home')
          else:
            messages.warning(request,f"The email is either invalid or already used to create an account")
    else:
      user_form = user_register_form()
      user_profile_form = user_register_profile_form()

    return render(request,'users/register.html', {'form':user_form, 'form1':user_profile_form, 'title':title})



# def login(request):
#     title= 'login'
     
#     if request.method == 'POST':
      
#             messages.success(request,f'Account created for {username}!')
#             return redirect('Omart-home')
#     else:
#       form = 

#     return render(request,'users/login.html', {'form':form, 'title':title})









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