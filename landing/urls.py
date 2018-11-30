from django.urls import path
from . import views
from events import urls as events_urls
from django.urls import path, include

urlpatterns = [
    path('', views.home),
    path('events',include(events_urls)),
    path('login',views.login1),
    path('login-submit',views.logging_in),
    path('signup',views.signup),
    path('signup_submit',views.signup_submit),
    path('logout',views.logout),

]