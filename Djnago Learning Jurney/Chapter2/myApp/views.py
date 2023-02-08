from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    a = "<h1> Hello Django Chapter 2 </h1>"
    return HttpResponse(a)
def myfirstFunction(request):
    return HttpResponse("Hello Django")

def learnDj(request):
    return HttpResponse("<h1> Hello Django Learn By Codex Coder</h1>")

def aboutMe(request):
    a = "hello! My Name is Codex Coder and I am a Python Developer"
    return HttpResponse(a)

def aboutDjango(request):
    about = '''Django is a Powerfull WebFrame Work that used to developed a Web Page
    usining Python.'''
    return HttpResponse(about)
