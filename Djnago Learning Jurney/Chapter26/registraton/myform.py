from django import forms 


class CourseRegistration(forms.Form):
    
    stuId = forms.IntegerField()
    name = forms.CharField()
    dob = forms.CharField()
    email = forms.EmailField()
    course = forms.CharField()
    
    
    
    