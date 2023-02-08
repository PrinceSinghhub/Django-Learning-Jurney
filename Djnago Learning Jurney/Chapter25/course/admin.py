from statistics import mode
from django.contrib import admin

from course import models

# register model using decorator 

@admin.register(models.Course)

# now create a model admin class and register for better data representation 

class courseAdmin(admin.ModelAdmin):
    
    list_display = ['stuid','stuName','branch','fees']


# without decorator register 
# admin.site.register(models.Course,courseAdmin)


