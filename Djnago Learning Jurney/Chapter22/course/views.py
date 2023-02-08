from django.shortcuts import render

# import out model class 
from course.models import Course

def course(request):
    # only particular data excess
    # studata = Course.objects.get(pk = 20222)
    # if we find a particular data then no need to use loop direst use variable AND print data like: 
    # studata.StuId 
    
   
    
    studata = Course.objects.all()
    print(studata)
    
    
    data = {'data': studata}
    
    return render(request,'course.html',data)


# Create your views here.


