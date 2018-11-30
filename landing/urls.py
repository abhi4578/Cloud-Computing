from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login',views.login1),
    path('login-submit',views.logging_in),
    path('signup',views.signup),
    path('signup_submit',views.signup_submit),
    path('logout',views.logout),

]