from . import views
from django.urls import path

urlpatterns = [     
    path('blog/', views.blogList.as_view(), name='blog'),
    path('<slug:slug>/', views.blogDetails.as_view(), name='blogdetails'),
]