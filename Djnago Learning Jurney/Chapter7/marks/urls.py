from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('indexm/',views.index),
    path('marks/',views.marks)
]



