from django.contrib import admin
from . import views
from .views import CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView
from django.urls import path
urlpatterns = [     
 
    path('register/',RegisterPage.as_view(), name='register'),
    # path('verify-email/<str:uidb64>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
]