from django.shortcuts import render

# Create your views here.

def index(request):
    
    a = "www.codexcoder.com"
    
    mydata = {'site':a}
    
    return render(request,'index.html',context=mydata)


def fees(request):
    
    mydata = {'btfee':150000,'aifee':250000,'itfee':75000,'mlfee':200000,'iotfee':70000}
    
    return render(request,'fee.html',context=mydata)


def course(request):
    
    mydata = {'c1':'B TECH','c2': 'AI','c3':"IT",'c4':'Machine Learning','c5':'IOT'}
    return render(request,'course.html',context=mydata)
    

