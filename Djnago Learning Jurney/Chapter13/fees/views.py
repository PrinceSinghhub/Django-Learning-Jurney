from django.shortcuts import render

# Create your views here.


def index(request):
    mydata = {'name':"Fees Index File"}
    return render(request,'fee.html',mydata)
