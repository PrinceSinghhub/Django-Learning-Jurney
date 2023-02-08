from time import time
from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponse
# Create your views here.

def index(request):
    
    a = "<h1><b>Hello! Django Chapter 10 Index File DTL Filter</b></h1>"
    return HttpResponse(a)
    

def Filters(request):
    
    Name = "codex coder"
    val = "Defalut Vaue"
    para = '''Django is a high-level Python web framework that encourages rapid development and clean,
    pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development,
    so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source. '''
    
    Date = datetime.now()
    
    Price = 58469.12345

    
    mydata = {'Name':Name,'val':val,'para':para,'Datetime':Date,'prince':Price}
    
    return render(request,'filters.html',mydata)
