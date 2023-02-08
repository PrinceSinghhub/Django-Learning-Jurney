from django.shortcuts import render

def home(request):
    
    return render(request,'home.html',{'def':'home'})

def about(request):
    
    return render(request,'about.html')

# Create your views here.
