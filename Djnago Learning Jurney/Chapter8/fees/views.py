from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request,'feeIndex.html')


def fee(request):
    return render(request,'fee.html')