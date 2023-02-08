from django.shortcuts import render

# Create your views here.


def index(request):
    
    return render(request,'index.html')


def student_info(request):
    # pass dynamic data in templates 

    
    mydata = {'id': '20ENG2CSE0079',
    'Name': "Codex Coder",
    'Branch': "B Tech",
    'DOB': "1 1 2002",
    'cont': '6265XXXX94'}
    
    return render(request,'data.html',context=mydata)