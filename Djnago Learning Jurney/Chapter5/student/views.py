from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def studentName(request):
    
    name = "Codex Coder"
    name1 = "Prince Singh"
    
    return HttpResponse([name, name1])
