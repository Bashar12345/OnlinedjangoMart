# from turtle import title
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .forms import user_registration_form

def register(request):
    title='SignUp'

    if request.method == 'POST':
      form = user_registration_form(request.POST)
      #print(form)
      if form.is_valid():
            print(form.cleaned_data)
            form.save()
          # username =form.cleaned_data.get('username') # username database e ase na need fixing
            username = form.cleaned_data['username']
            print(username)
            messages.success(request,f'Account created for {username}!')
            return redirect('Omart-home')
    else:
      form = user_registration_form()

    return render(request,'users/register.html', {'form':form, 'title':title})
