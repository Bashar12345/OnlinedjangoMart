from django.shortcuts import render
#from .


# Create your views here.
def register(request):
    form = user_registration_form() 
    return render(request,'users/register.html',{'form':form})
