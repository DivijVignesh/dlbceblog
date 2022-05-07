from dataclasses import field, fields
from datetime import date
import email
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from authentication.models import account
from blogapp.models import Blogmaster, Tblprofile , Tblcomments
# Create your forms here.



class ProfileEdit(forms.ModelForm):
    # username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Username','id':'username' }),)

    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Email', }),)
    batch= forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Year of joining'}),)
    # phoneno= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Phone Number'}),)
    fullname= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Full Name'}),)
    branch= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Branch'}),)
    rollno= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Roll number'}),)
    classname = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'classname'}),)
    # password2 = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'type':'password','placeholder': 'Password again'}),)
    image = forms.ImageField()
    class Meta:
        model= Tblprofile
        fields=["email","batch","fullname","branch","rollno","classname","image"]

class BlogUpload(forms.ModelForm):
    title = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Title', }),)
    quote= forms.CharField(required=True,max_length=10000,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Quote'}),)
    matter= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Matter'}),)
    description= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Description'}),)
    photo= forms.ImageField()
    class Meta:
        model= Blogmaster
        fields=["title","quote","matter","description", "photo"]       
    
class BlogUpdate(forms.ModelForm):
    title = forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Title', }),)
    quote= forms.CharField(required=True,max_length=10000,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Quote'}),)
    matter= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Matter'}),)
    description= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Description'}),)
    photo= forms.ImageField()
    class Meta:
        model= Blogmaster
        fields=["title","quote","matter","description", "photo"]   

class AddComment(forms.ModelForm):
    comment= forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Query Here', }),)

    class Meta:
        model= Tblcomments
        fields=["comment"]
