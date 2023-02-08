from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    a = "<h1>Hello Django Chapter 4</h1>"
    
    return HttpResponse(a)


def aboutDj(request):
    
    para = '''Django is a high-level Python web framework that encourages rapid development and clean, 
    pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, 
    so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.'''
    
    return HttpResponse(para)

def aboutMe(request):
    
    me = "Hello! My Name is <b>CODE CODER</b> I am Python Programmer"
    return HttpResponse(me)
    
