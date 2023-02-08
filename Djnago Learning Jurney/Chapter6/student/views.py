from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    a = "<h1>Hello Django Chapter 6 Student File</h1>"
    
    return HttpResponse(a)

def student(request):
    
    return HttpResponse("Codex Coder")