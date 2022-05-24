from multiprocessing import context
from django.http import HttpResponse
from ast import Add
from django.shortcuts import render, redirect
import mysql.connector
from django.contrib import messages
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from blogapp.forms import   AddComment, BlogUpload
from blogapp.models import Blogmaster, Tblcomments, Usermain
config = {
    'user': 'divij',
    'password': 'divijak-47',
    'host': 'divij.mysql.pythonanywhere-services.com',
    'database': 'divij$default'
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
    query=(" select username from blogmaster join tblprofile on tblprofile.userid= blogmaster.userid where blogid={} and isdeleted=0").format(blogid)
    cursor.execute(query)
    # print(cursor)
    com=[]
    for id in cursor:
        com.append(id)
        # print(id)
    if(len(com)==0):
        return redirect('/profile/'+str(username)) #redirect when wrong blog id is entered
    # print(com[0][0])
    if com[0][0] != username:
        return HttpResponse("Page not found", content_type='text/plain')
    if request.method == 'GET':
        query=(" select tblprofile.username,firstname, lastname,blogmaster.userid, title ,description,quote,matter,blogid,CONVERT_TZ (timeofupload,'+00:00','+05:30'),photo,image, views from usermain join blogmaster on usermain.id = blogmaster.userid join tblprofile on tblprofile.userid= usermain.id where tblprofile.username='{}' and blogid='{}'").format(username,blogid)
        cursor.execute(query)
        form = AddComment()
        # results = next(cursor.stored_results()).fetchall()
        # print(cursor)
        idd=[]
        for id in cursor:
            idd.append(id)
            # print(id)
        # print(idd)

        query=("select TIMESTAMPDIFF(MINUTE, tblcomments.timeofupload,NOW()),tblcomments.commentid,tblprofile.username, comment ,tblprofile.image ,tblprofile.fullname from tblcomments join blogmaster on tblcomments.blogid = blogmaster.blogid join tblprofile on tblcomments.userid = tblprofile.userid where tblcomments.blogid={};").format(blogid)
        cursor.execute(query)
        # print(cursor)
        com=[]
        for id in cursor:
            com.append(id)
            # print(id)
        # print(com)
        cursor.close()
        cnx.commit()
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        query=(' UPDATE blogmaster set views= views+1 where blogid={}').format(blogid)
        cursor.execute(query)
        # obj = get_object_or_404(Blogmaster, blogid=blogid)
        # views= obj.views
        # print("Views is:"+str(views))
        # obj.views= views+1
        # obj.save()
        cursor.close()
        cnx.commit()
        print("update")
        return render(request,'blogtemplate.html', {
            'blog': idd,
            'form':form,
            'comment':com
            }
        )
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            obj = get_object_or_404(Usermain, username=request.user.username)
            userid= obj.id
            query=('insert into tblcomments(blogid, userid,comment) values ({},{},{})').format(blogid,userid,"'"+comment+"'")
            cursor.execute(query)
            cursor.close()
            cnx.commit()
            return redirect("/"+str(username)+"/"+str(blogid))

        else:
            # print('Form is not valid')
            # messages.error(request, 'Error Processing Your Request')
            return redirect("/"+str(username)+"/"+str(blogid))



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
            # print(userid)

            userid= Usermain.objects.get(pk=userid)
            obj = Blogmaster(title = title,
                description = description,
                quote = quote,
                matter= matter,
                photo= photo,
                userid =userid,
                views=1)
            obj.save()

            return redirect('profile/'+str(username))
        else:
            # print('Form is not valid')
            # messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'blogtemplateupload.html', context)

def blog_update(request,username,blogid):
    if request.user.username == username:
        # dictionary for initial data with
        # field names as keys
        context={}



        # fetch the object related to passed id
        # obj = get_object_or_404(Blogmaster, blogid=blogid)
        # # pass the object as instance in form

        obje= Blogmaster.objects.filter(blogid=blogid)
        # pass the object as instance in form
        # print(obje)
        if not obje:
            return HttpResponseRedirect('/profile')
        obj= get_object_or_404(obje)

        form = BlogUpload(request.POST or None,request.FILES or None, instance = obj)

        # save the data from the form and
        # redirect to detail_view
        if form.is_valid():
            form.save()
            # print("form is valid")
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
        # query=('delete from blogmaster where blogid={}').format(blogid)
        query=('update blogmaster set isdeleted=1 where blogid={}').format(blogid)
        cursor.execute(query)
        cnx.commit()
        # Blogmaster.objects.filter(blogid=blogid).delete()
        print("Deleted blog with id"+str(blogid))
        # obje= Blogmaster.objects.filter(blogid=blogid)
        # if not obje:
        #     return redirect('/profile')
        # else:
        #     return redirect('/'+username+'/'+str(blogid)+'/delete')
        return redirect('/profile')
    return redirect('/profile')

def blogs(request):

    com=[]
    context={}

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query=(" select blogid,title,description, matter,quote, CONVERT_TZ (timeofupload,'+00:00','+05:30'),photo,views, username,image, fullname from blogmaster join tblprofile on blogmaster.userid= tblprofile.userid and isdeleted =0")
    cursor.execute(query)
    for id in cursor:
            com.append(id)
            # print(id)
    # print(com)
    context['blogs']= com
    return render(request,"mainblog.html", context)
