from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class Registration(forms.Form):
    firstname=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'name': "firstname", 'class':"form-control"}))
    lastname=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'name': "lastname", 'class':"form-control"}))
    email=forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'name': "email", 'class':"form-control"}))
    username=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'name': "username", 'class':"form-control"}))
    password=forms.CharField(widget=(forms.PasswordInput(attrs={'name':"passwords", 'class':"form-control", 'type':"password"})))
    re_password=forms.CharField(widget=forms.PasswordInput(attrs={'name': "re_password", 'class': "form-control", 'type' : "password"}))

   
    