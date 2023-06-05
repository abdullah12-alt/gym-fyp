from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('<int:amount>/', views.payment, name='payment'),
    
        # Other payment app URL patterns...
   
]
    
