from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView

class HomePageView(TemplateView): #instead of def we create class "classes sshould be capitalized"
 template_name = "home.html"

class AboutPageView(TemplateView): 
 template_name = "about.html"

'''
from django.http import HttpResponse
def homePageView(request):
    return HttpResponse("Hello, World!")'''