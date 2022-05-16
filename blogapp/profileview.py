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
    query = ("SELECT fullname, branch,rollno, username, image from tblprofile where fullname is not null" )
    cursor.execute(query)
    # results = next(cursor.stored_results()).fetchall()
    print(cursor)
    idd=[]
    for id in cursor:
        idd.append(id)
        # print(id)
    print(idd)
    
    query = ("select title, description,quote,photo,views,TIMESTAMPDIFF(MINUTE,timeofupload,NOW()),username,blogid from blogmaster join tblprofile on blogmaster.userid=tblprofile.userid order by views DESC  limit 4" )
    cursor.execute(query)
    # results = next(cursor.stored_results()).fetchall()
    print(cursor)
    blog=[]
    for id in cursor:
        blog.append(id)
        # print(id)
    print(blog)
    cursor.close()
    return render(request,'bloghomepage.html', {
        'account': idd,
        'blogs':blog
        }
    )

def profileview(request,username):
    # redirect to user profile view if the request is from owner 
    if request.user.username== username:
        return HttpResponseRedirect("/profile/") 
        
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    # query = ("SELECT fullname, phone,branch,batch,rollno,classname,email,username from tblprofile")

    query = ("SELECT fullname,branch,batch,rollno,classname,email,username,image from tblprofile where username='"+username+"'")
    cursor.execute(query)
    # results = next(cursor.stored_results()).fetchall()
    print(cursor)
    idd=[]
    di=my_dictionary()
    for id in cursor:
        my_dictionary.add(di,'profile',id)  
    query = ('select userid, title ,description,quote,matter ,blogid,photo,TIMESTAMPDIFF(MINUTE, timeofupload,NOW()),views, username from usermain join blogmaster on usermain.id = blogmaster.userid where username="{}"').format(username)
    cursor.execute(query)
    for id in cursor:
        idd.append(id)
    print(idd)
    my_dictionary.add(di,'blogs',idd)
    cursor.close()
    return render(request,'profile.html', {
        'account': di
        }
    )

def userprofileview(request):
    
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    # query = ("SELECT fullname, phone,branch,batch,rollno,classname,email,username from tblprofile")

    query = ("SELECT fullname,branch,batch,rollno,classname,email,username,image from tblprofile where username={}").format("'"+request.user.username+"'")
    cursor.execute(query)
    # results = next(cursor.stored_results()).fetchall()
    print(cursor)
    idd=[]
    di=my_dictionary()
    for id in cursor:
        my_dictionary.add(di,'profile',id)  
    query = ('select userid, title ,description,quote,matter ,blogid, photo,TIMESTAMPDIFF(MINUTE, timeofupload,NOW()),views from usermain join blogmaster on usermain.id = blogmaster.userid where username="{}"').format(request.user.username)
    cursor.execute(query)
    for id in cursor:
        idd.append(id)
    print(idd)
    my_dictionary.add(di,'blogs',idd)
    cursor.close()
    return render(request,'userprofile.html', {
        'account': di
        }
    )

def update_view(request):
    # dictionary for initial data with
    # field names as keys
    context={}
    
        
 
    # fetch the object related to passed id
    obj = get_object_or_404(Tblprofile, username = request.user.username)
    # pass the object as instance in form
    form = ProfileEdit(request.POST or None,request.FILES or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        print("form is valid")
        return HttpResponseRedirect("/profile/"+request.user.username)
 
    # add form dictionary to context
    context["form"] = form
    context["obj"]=obj
 
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