from django.urls import path

from . import views


urlpatterns = [

    path('', views.index, name="index"),
    path('process', views.processed, name="processed"),
    path('process1', views.process1, name="process1")
]