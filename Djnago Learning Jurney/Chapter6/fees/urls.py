from django.contrib import admin
from django.urls import path

from fees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('indexf/',views.index),
    path('fee/',views.fee),

    
]