from django.shortcuts import render


def home(request):
    
    return render(request,'home.html')

def chapter15(request):
    return render(request,'Chpater15.html')