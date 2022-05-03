
from django.http import request
from django.shortcuts import render , redirect
from django.views.generic import ListView, TemplateView

from .forms import NewUserForm, SignupForm ,UserCreationForm

from django.contrib import messages


from django.shortcuts import render, redirect
import mysql.connector


from django.contrib import messages

config = {
    'user': 'djangouser',
    'password': 'password',
    'host': 'localhost',
    'database': 'lbceblog'
}



def signup_request(request):
    if request.method == 'GET':
        form  = NewUserForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    if request.method == 'POST':
        form  = NewUserForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('firstname')
            email = form.cleaned_data.get('email')
            yearofjoining= form.cleaned_data.get('yearofjoining')
            phoneno= form.cleaned_data.get('phoneno')
            rollno =form.cleaned_data.get('rollno')
            lastname= form.cleaned_data.get('lastname')
            username= form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            print(firstname)
            form.save()
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            # query = ("INSERT into usermain(email, firstname,lastname, yearofjoining,phoneno,rollno,username) values ('{}','{}','{}','{}','{}','{}','{}')").format(email, firstname,lastname, yearofjoining,phoneno,rollno,username)
            # cursor.execute(query)
            cursor.callproc("insert_user_and_profile",[email,firstname,lastname,yearofjoining,phoneno,rollno,username])
            for r in cursor:
                print(type(r))
                print(firstname)
            
            cnx.commit()
            
            return render(request, 'login.html', context={}) 
        else:   
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'signup.html', context)

