from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index),
    # <a style="color:white" href='/stars/{{star.starName}}'>

]
