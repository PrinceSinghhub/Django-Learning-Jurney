from django.shortcuts import render


from django.http  import HttpRequest, HttpResponse
# Create your views here.

def index(request):
    a = "<h1>Hello Django Chapter 5</h1>"
    
    return HttpResponse(a)

def course(request):
    a = "B TECH CSE IV SEM"
    
    return HttpResponse(a)
    
    
