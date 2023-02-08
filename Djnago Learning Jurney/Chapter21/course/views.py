import re
from django.shortcuts import render

def home(request):
    
    return render(request,'home.html')

def course(request):
    
    return render(request,'course.html')

# Create your views here.
