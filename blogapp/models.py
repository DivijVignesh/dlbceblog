import email
from email.policy import default
from django.db import models

# Create your models here.
from django.urls import reverse


class Tblprofile(models.Model):
    fullname = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    branch = models.CharField(max_length=20, blank=True, null=True)
    batch = models.CharField(max_length=20, blank=True, null=True)
    rollno = models.CharField(max_length=20, blank=True, null=True)
    classname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=20)
    userid = models.IntegerField(blank=True, null=True)

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

    class Meta:
        managed = False
        db_table = 'usermain'