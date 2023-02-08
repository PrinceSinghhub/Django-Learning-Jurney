from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    a = "<h1>Hello Django Chapter 3</h1>"
    
    return HttpResponse(a)
    
    