from re import T
from django.db import models

# my model class of course 
class Course(models.Model):
    
    courseId = models.IntegerField(primary_key=True)
    courseName = models.CharField(max_length=50)
    branchName = models.CharField(max_length=10)
    
    # udate our models after create a model 
    courseDate = models.CharField(max_length=20,default='not available')
    
    

# Create your models here.
