from django.shortcuts import render

# Create your views here.


def index(request):
    mydata = {'name':"Coursr Index File"}
    return render(request,'course.html',mydata)
