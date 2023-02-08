from django.shortcuts import render

# Create your views here my code here

def index(request):
    
    return render(request,'courseIndex.html')

def course(request):
    
    return render(request,'course.html')




