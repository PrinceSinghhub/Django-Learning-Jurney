from django.urls import path

from . import views

urlpatterns = [
    path('courseIndex/',views.index,name='course'),
]