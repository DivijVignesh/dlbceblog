
from django.shortcuts import render, redirect
import mysql.connector
from django.contrib import messages
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from blogapp.forms import BlogUpload
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
    query=(' select username,firstname, lastname,userid, title ,description,quote,matter,blogid from usermain join blogmaster on usermain.id = blogmaster.userid where username="{}" and blogid="{}"').format(username,blogid)
    cursor.execute(query)
    # results = next(cursor.stored_results()).fetchall()
    print(cursor)
    idd=[]
    for id in cursor:
        idd.append(id)
        # print(id)
    print(idd)
    cursor.close()
    return render(request,'blogtemplate.html', {
        'blog': idd
        }
    )
    
def blogupload(request):
    if request.method == 'GET':
        form  = BlogUpload()
        context = {'form': form}
        return render(request, 'blogtemplateupdate.html', context)
    if request.method == 'POST':
        form  = BlogUpload(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            quote= form.cleaned_data.get('quote')
            matter= form.cleaned_data.get('matter')
            username= request.user.username
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            query=('select id from usermain where username="{}"').format(username)
            cursor.execute(query)
            id=[]
            for r in cursor:
                id.append(r)
            userid= id[0][0]
            
            
            print(userid)
            query=('INSERT INTO blogmaster (userid, title, description, matter, quote) VALUES ("{}", "{}", "{}", "{}", "{}");').format(userid,title,description,matter,quote)
            cursor.execute(query)
            # form.save()
            cnx.commit()
            
            return redirect('profile/'+str(username))
        else:   
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'blogtemplateupdate.html', context)