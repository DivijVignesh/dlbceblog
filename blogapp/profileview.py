import base64
from multiprocessing import context
from unittest import result
from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
import json
from blogapp.forms import ProfileEdit
from blogapp.models import Tblprofile
# import win32api
from datetime import datetime
import mysql.connector
from django.contrib import messages
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
config = {
    'user': 'djangouser',
    'password': 'password',
    'host': 'localhost',
    'database': 'lbceblog'
}


# Create your views here.


class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value
def template(request):
    context={}
    return render(request,'template.html', {
        'account': context
        }
    ) 
def profilehome(request):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("SELECT fullname, branch,rollno, username from tblprofile where fullname is not null" )
    cursor.execute(query)
    # results = next(cursor.stored_results()).fetchall()
    print(cursor)
    di={}
    di=my_dictionary()
    my_dictionary.add(di,0,"first")
    my_dictionary.add(di,'1',"Second") 
    print(di['1'])
    idd=[]
    for id in cursor:
        idd.append(id)
        print(id)
    print(idd)
    cursor.close()
    return render(request,'bloghomepage.html', {
        'account': idd
        }
    )

def profileview(request,username):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    # query = ("SELECT fullname, phone,branch,batch,rollno,classname,email,username from tblprofile")

    query = ("SELECT fullname,branch,batch,rollno,classname,email,username from tblprofile where username='"+username+"'")
    cursor.execute(query)
    # results = next(cursor.stored_results()).fetchall()
    print(cursor)
    idd=[]
    for id in cursor:
        idd.append(id)
        print(idd)
        print(type(idd))
    print(idd)
    cursor.close()
    return render(request,'profile.html', {
        'account': id
        }
    )

def update_view(request, username):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Tblprofile, username = username)
 
    # pass the object as instance in form
    form = ProfileEdit(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        print("form is valid")
        return HttpResponseRedirect("/profile/"+username)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "profileedit.html", context) 
def profileedit(request):
    if request.method == 'GET':
        form  = ProfileEdit()
        context = {'form': form}
        return render(request, 'signup.html', context)
    if request.method == 'POST':
        form  = ProfileEdit(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data.get('fullname')
            email = form.cleaned_data.get('email')
            batch= form.cleaned_data.get('batch')
            classname= form.cleaned_data.get('classname')
            rollno =form.cleaned_data.get('rollno')
            lastname= form.cleaned_data.get('lastname')
            branch = form.cleaned_data.get('branch')

            print(fullname)
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            query = ("INSERT into usermain(email, firstname,lastname, yearofjoining,phoneno,rollno) values ('{}','{}','{}','{}','{}','{}')").format(email, firstname,lastname, yearofjoining,phoneno,rollno)
            cursor.execute(query)
            for r in cursor:
                print(type(r))
                print(fullname)
            form.save()
            cnx.commit()
            
            return redirect('login')
        else:   
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'signup.html', context)