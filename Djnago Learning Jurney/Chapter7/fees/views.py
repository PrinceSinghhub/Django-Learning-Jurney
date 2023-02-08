from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    a = "<h1>Hello Django Chapter 7 Fee File</h1>"
    
    return HttpResponse(a)


def fee(request):
    a = ["B tech: 150000","AI:2000000","ML:2500000","B tech Code: 100000"]
    
    return HttpResponse(a)