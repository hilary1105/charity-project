from django.contrib import admin
from django.urls import path
from charityfinder import views

urlpatterns = [
path('', views.index, name="index"),
path('insert', views.insertData, name="insertData"),
]