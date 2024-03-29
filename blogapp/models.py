import email
from email.policy import default
from django.db import models

# Create your models here.
from django.urls import reverse


class Tblprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    batch = models.CharField(max_length=20, blank=True, null=True)
    rollno = models.CharField(max_length=20, blank=True, null=True)
    classname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=20)
    userid = models.IntegerField()
    image = models.ImageField(upload_to='users/profile')
    class Meta:
        managed = False
        db_table = 'tblprofile'

class Blogmaster(models.Model):
    blogid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Usermain', models.DO_NOTHING, db_column='userid')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    matter = models.CharField(max_length=10000)
    quote = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='users/')
    views = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'blogmaster'

class Usermain(models.Model):
    email = models.CharField(max_length=45, blank=True, null=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    yearofjoining = models.CharField(max_length=45, blank=True, null=True)
    phoneno = models.CharField(max_length=45, blank=True, null=True)
    rollno = models.CharField(max_length=45, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    role= models.CharField(max_length=45,blank=True)
    class Meta:
        managed = False
        db_table = 'usermain'

class Tblcomments(models.Model):
    commentid = models.AutoField(primary_key=True)
    blogid = models.IntegerField()
    userid = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblcomments'