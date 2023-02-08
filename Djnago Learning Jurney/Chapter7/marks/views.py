from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    a = "<h1>Hello Django Chapter 7 marks File</h1>"
    
    return HttpResponse(a)


def marks(request):
    a = ["Python: 98","Java: 80","C: 70","ML: 89"]
    
    return HttpResponse(a)