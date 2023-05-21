from django.contrib import admin
from . import views
from django.urls import path
urlpatterns = [     
    path('', views.login , name="login"),
    path('signup', views.signup , name="signup"),
    path('signout', views.signout , name="signout"),
]