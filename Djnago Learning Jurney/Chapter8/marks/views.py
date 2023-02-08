from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request,'marksIndex.html')


def marks(request):
    return render(request,'marks.html')