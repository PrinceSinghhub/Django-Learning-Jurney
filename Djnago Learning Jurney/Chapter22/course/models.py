from statistics import mode
from django.db import models

class Course(models.Model):
    
    StuId = models.IntegerField(primary_key=True)
    StuName = models.CharField(max_length=30)
    StuBranch = models.CharField(max_length=20)
    StuFee = models.IntegerField()
 
    

# Create your models here.
