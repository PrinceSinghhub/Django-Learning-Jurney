from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('indexc/',views.index),
    path('course/',views.course)
]


 
