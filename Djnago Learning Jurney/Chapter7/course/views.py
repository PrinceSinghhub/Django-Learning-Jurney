from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    a = "<h1>Hello Django Chapter 7 Course File</h1>"
    
    return HttpResponse(a)

def course(request):
    
    return HttpResponse("B Tech CSE")
