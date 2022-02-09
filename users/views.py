# from turtle import title
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib import messages
from matplotlib.pyplot import title
from .forms import user_registration_form,user_login_form

def register(request):
    title='SignUp'

    if request.method == 'POST':
      form = user_registration_form(request.POST or None)
      if form.is_valid():
            print(form.cleaned_data)
            form.save()
            username =form.cleaned_data.get('username') # username database e ase na 
          # need fixing
            print(username)
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # print(username)
            # print(email)
            messages.success(request,f'Account created for {username}!')
            return redirect('Omart-home')
    else:
      form = user_registration_form()

    return render(request,'users/register.html', {'form':form, 'title':title})

def login(request):
    title= 'login'
     
    if request.method == 'POST':
      form = user_login_form(request.POST or None)
      if form.is_valid():
            print(form.cleaned_data)
            form.save()
            username =form.cleaned_data.get('username') # username database e ase na 
          # need fixing
            print(username)
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # print(username)
            # print(email)
            messages.success(request,f'Account created for {username}!')
            return redirect('Omart-home')
    else:
      form = user_login_form()

    return render(request,'users/login.html', {'form':form, 'title':title})
