from django.contrib import admin
from . import views
from .views import CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView
from django.urls import path
urlpatterns = [     
 
    path('signup/',RegisterPage.as_view(), name='signup'),
    path('',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
]