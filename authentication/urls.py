from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from authentication import signup
from . import views

from .views import HomeView
urlpatterns = [    
    # path('signup/', views.register_request, name='signup'),

    path('signup/', signup.signup_request, name='signup'),
    path('', views.login_request,name='login'),
    path("logout", views.logout_request, name= "logout"),
]