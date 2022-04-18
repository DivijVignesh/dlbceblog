from datetime import date
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from authentication.models import account
# Create your forms here.

class SignupForm(forms.Form):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Email', }),)
    yearofjoining= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Year of joining'}),)
    phoneno= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Phone Number'}),)
    firstname= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'First Name'}),)
    lastname= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Last Name'}),)
    password1 = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Password'}),)
    password2 = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Password again'}),)
    rollno= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Roll number'}),)
    # branch= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'First Name'}),)


    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        firstname = cleaned_data.get('lastname')
        lastname = cleaned_data.get('lastname')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        # if not name and not email and not message:
        #     raise forms.ValidationError('You have to write something!')

class NewUserForm(UserCreationForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Username','id':'username' }),)

    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Email', }),)
    yearofjoining= forms.CharField(required=True,max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Year of joining'}),)
    phoneno= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Phone Number'}),)
    firstname= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'First Name'}),)
    lastname= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Last Name'}),)
    rollno= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Roll number'}),)
    password1 = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg','type':'password', 'placeholder': 'Password'}),)
    password2 = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'type':'password','placeholder': 'Password again'}),)
    
    class Meta:
        model = User
        fields = ("firstname", "lastname","email","phoneno", "password1", "password2","rollno","yearofjoining", "username")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['firstname']
        user.first_name= self.cleaned_data['firstname']
        user.last_name= self.cleaned_data['lastname']
        if commit:
            user.save()
        return user
        
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control lg', 'placeholder': 'username', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control form-control lg',
            'placeholder': 'password',
            'id': 'password',
        }
))