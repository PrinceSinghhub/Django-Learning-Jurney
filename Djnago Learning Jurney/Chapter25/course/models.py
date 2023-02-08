from django.db import models

# Create your models here.

class Course(models.Model):
    
    stuid = models.IntegerField(primary_key=True)
    stuName = models.CharField(max_length=30)
    branch = models.CharField(max_length=10)
    fees = models.IntegerField()
    
    # def __str__(self):
        
    #     return str(self.stuid)
    
    
