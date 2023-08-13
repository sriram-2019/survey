from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from main import views
urlpatterns = [
    path('',views.inde,name='')
]