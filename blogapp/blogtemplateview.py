
from django.shortcuts import render, redirect
import mysql.connector
from django.contrib import messages
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from blogapp.forms import   BlogUpload
from blogapp.models import Blogmaster, Usermain
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

def blogview(request, username , blogid):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query=(' select username,firstname, lastname,userid, title ,description,quote,matter,blogid,timeofupload,photo, views from usermain join blogmaster on usermain.id = blogmaster.userid where username="{}" and blogid="{}"').format(username,blogid)
    cursor.execute(query)
    
    # results = next(cursor.stored_results()).fetchall()
    print(cursor)
    idd=[]
    for id in cursor:
        idd.append(id)
        # print(id)
    print(idd)
    query=(' UPDATE blogmaster set views= views+1 where blogid={}').format(blogid)
    cursor.execute(query)
    cursor.close()
    cnx.commit()
    return render(request,'blogtemplate.html', {
        'blog': idd
        }
    )
    
def blogupload(request):
    if request.method == 'GET':
        form  = BlogUpload()
        context = {'form': form}
        return render(request, 'blogtemplateupload.html', context)
    if request.method == 'POST':
        form  = BlogUpload(request.POST or None, request.FILES or None)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            quote= form.cleaned_data.get('quote')
            matter= form.cleaned_data.get('matter')
            username= request.user.username
            photo= form.cleaned_data.get('photo')
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            query=('select id from usermain where username="{}"').format(username)
            cursor.execute(query)
            id=[]
            for r in cursor:
                id.append(r)
            userid= id[0][0]
            print(userid)
            
            userid= Usermain.objects.get(pk=userid)
            obj = Blogmaster(title = title,  
                description = description,
                quote = quote,
                matter= matter,
                photo= photo,
                userid =userid  )
            obj.save()

            return redirect('profile/'+str(username))
        else:   
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'blogtemplateupload.html', context)

def blog_update(request,username,blogid):
    if request.user.username == username:
        # dictionary for initial data with
        # field names as keys
        context={}
        
            
    
        # fetch the object related to passed id
        obj = get_object_or_404(Blogmaster, blogid=blogid)
        # pass the object as instance in form
        form = BlogUpload(request.POST or None,request.FILES or None, instance = obj)
    
        # save the data from the form and
        # redirect to detail_view
        if form.is_valid():
            form.save()
            print("form is valid")
            return HttpResponseRedirect("/"+request.user.username+"/"+str(blogid))
    
        # add form dictionary to context
        context["form"] = form
        context["obj"]=obj
    
        return render(request, "blogtemplateupdate.html", context) 
    else:
        return HttpResponseRedirect("/"+request.user.username+"/"+str(blogid)) 
    
def blog_delete(request,username,blogid):

    if request.user.username==username:

        
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        query=('delete from blogmaster where blogid="{}"').format(blogid)
        cursor.execute(query)
        cnx.commit()
        return redirect('/profile')
