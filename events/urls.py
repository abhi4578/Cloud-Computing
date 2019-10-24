from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index),
    path('marker',views.mapMarker, name="marker"),
    path('comment',views.comments),
    path('twitter',views.twitter),
    path('<str:eventId>',views.eventDetail,name="id"),
    

    # <a style="color:white" href='/stars/{{star.starName}}'>

]
