from django.shortcuts import render

def index(request):
    
    return render(request,'index.html')

# create our django form class object 
from . import myform

def showData(request):
    
    obj = myform.CourseRegistration()
    data = {'form':obj}
    return render(request,'registration.html',data)

# Create your views here.
