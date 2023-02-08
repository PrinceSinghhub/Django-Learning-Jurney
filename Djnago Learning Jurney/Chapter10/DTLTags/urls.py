from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('index',views.index),
    path('ifTags/',views.ifTags),
    path('looptags/',views.loopTag),
    path('ndata/',views.netedData),
    path('keyData/',views.keyValue)
    
    
    
]
