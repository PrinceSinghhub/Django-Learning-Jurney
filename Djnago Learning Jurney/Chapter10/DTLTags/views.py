from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
# Create your views here.

def index(request):
    
    a = "<h1><b>Hello! Django Chapter 10 Index File DTL Tags</b></h1>"
    return HttpResponse(a)

def ifTags(request):
    
    def check_primeorNot(num):
        
        if num < 2:
            return False
        
        count = 2
        
        while count * count <= num:
            if num%count == 0:
                return False
            count+=1
            
        return True
    
    def even_old(num):
        
        if num % 2 == 0:
            return True
        else:
            return False
        
        

    n = 7
    
    # todo check even or old 
    num = 71
    ans = even_old(num)
    
    # prime or not
    num1 = 2
    ans1 = check_primeorNot(num1) 
    
    mydata = {'n':n,'ans':ans,'num':num,'ans1':ans1,'num1':num1}
    return render(request,'iftags.html',context=mydata)
    
    
def loopTag(request):
    
    # for nth natureal number 
    n = 10
    naturalnum = []
    
    for i in range(1,n+1):
        naturalnum.append(i)
    
    
    student = {'name':['Codex Coder','Prince Singh','Coder','Codex'],'nn':naturalnum}
    
    return render(request,'looptags.html',student)


def netedData(request):
    
    student = {'stu1':{'name':'Codex Coder','rn':'s1101'},
               'stu2':{'name':'Coder','rn':'s2102'},
               'stu3':{'name':'Codex','rn':'s3103'},
               'stu4':{'name':'C Codex','rn':'s4104'}}
    
    mydata = {'stuData':student}
    return render(request,'nested_dic_data.html',mydata)

def keyValue(request):
    
    student = {'stu1':{'name':'Codex Coder','rn':'s1101'},
               'stu2':{'name':'Coder','rn':'s2102'},
               'stu3':{'name':'Codex','rn':'s3103'},
               'stu4':{'name':'C Codex','rn':'s4104'}}
    
    mydata = {'data':student}
    return render(request,'key_value.html',mydata)
    