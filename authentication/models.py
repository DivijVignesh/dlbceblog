from django.db import models
from django.urls import reverse
# Create your models here.
class account(models.Model):
    firstname = models.CharField(max_length=50, db_collation='utf8_general_ci')
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phoneno = models.CharField(max_length=50, default="900009")
    rollno = models.CharField(max_length=50, default="3201364100")
    yearofjoining = models.CharField(max_length=50 ,default="2020-2024")
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20) 
    username = models.CharField(max_length=20, default="null") 
    def __str__(self):
        return self.title
    def get_absolute_url(self): 
        return reverse('home', args=[str(self.id)])