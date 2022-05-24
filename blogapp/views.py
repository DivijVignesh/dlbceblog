from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView ,DetailView
import json
# from blogapp.models import Profile
from . import profileview
# Create your views here.
class HomeView(TemplateView):
    template_name= 'bloghomepage.html'

def aboutus(request):
    context={}
    return render(request,'about.html', {
        'account': context
        }
    )

# class ProfileView(TemplateView):
#     template_name= 'profile.html'

# class MobileDataView(DetailView):
#     model=Profile
#     template_name='profile.html'

# def view(request,pk):
#     obj=Profile.objects.all()
#     # s=json.dumps(obj)
#     # print("myoutput",obj)

#     return render(request,'profile.html', {
#     'profile': Profile.objects.get(id=pk)
#     }
# )