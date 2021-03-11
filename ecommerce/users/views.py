from django.shortcuts import render, redirect
from . import forms
from .models import Users
from django.core.exceptions import ValidationError
# Create your views here.

def regform(request):
    form=forms.Registration()
    
    if request.method == 'POST':

        form=forms.Registration(request.POST)

        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            email=form.cleaned_data['email']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            re_password=form.cleaned_data['re_password']
            msg_status1=True
            if password != re_password:
                msg_status=False
                message="Passwordlar uygun deyil"
                return render(request, 'accounts/registration.html', {'message': message, 'form':form})
            else:
                keep=Users(firstname=firstname, lastname=lastname, email=email, username=username, password=password)
                keep.save()

    context={
        'form' : form,
        }

    return render(request, 'accounts/registration.html', context)
