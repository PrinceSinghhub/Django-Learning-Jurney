from django.shortcuts import render

# Create your views here.

def index(request):
    
    mydata = {'id':'20END2CSE0079','name':'Codex Coder','branch':'Computer Science','dob':"1:1:2002",'cn':6265233494}
    
    return render(request,'studentInfo.html',context=mydata)
