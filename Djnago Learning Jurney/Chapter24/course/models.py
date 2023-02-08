from django.db import models

# Create your models here.
class course(models.Model):

    stuId = models.IntegerField(primary_key = True)
    stuName = models.CharField(max_length = 30)
    courseName = models.CharField(max_length = 50)


    def __str__(self):

        return self.stuName