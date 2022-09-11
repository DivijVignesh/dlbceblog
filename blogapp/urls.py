from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import blogtemplateview



from . import profileview
from . import views
urlpatterns = [
    # path('',HomeView.as_view(),name='home'),
    path('',profileview.profilehome,name='home'),
    path('profile/edit/', profileview.update_view, name='profileedit'),
    # path('profile/<int:pk>/', MobileDataView.as_view(), name='profileview'),
    path('profile/<str:username>/',profileview.profileview,name='profile'),   # profile url
    path('profile/',profileview.userprofileview,name='profile'),
    path('msindhu/template', profileview.template, name="blogtemplate"),
    path('<str:username>/<int:blogid>', blogtemplateview.blogview , name="blogview"),
    path('add', blogtemplateview.blogupload , name="blogadd"),
    path('<str:username>/<int:blogid>/edit', blogtemplateview.blog_update , name="blogedit"),
    path('<str:username>/<int:blogid>/delete', blogtemplateview.blog_delete , name="blogedit"),
    path('blogs', blogtemplateview.blogs , name="blogdisplay"),
    path('aboutus',views.aboutus, name="aboutus"),
    path('events',views.events, name="events"),

]
