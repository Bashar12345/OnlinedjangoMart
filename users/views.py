# from turtle import title
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    title='SignUp'

    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
          form.save()
          username =form.cleaned_data.get('username') # username database e ase na need fixing
          messages.success(request,f'Account created for {username}!')
          return redirect('Omart-home')
    else:
      form=UserCreationForm()

    return render(request,'users/register.html', {'form':form, 'title':title})
