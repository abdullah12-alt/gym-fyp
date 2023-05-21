"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from myproject import views
urlpatterns = [
    path('admin/', admin.site.urls),
     path('logout/', RedirectView.as_view(url = '/admin/logout/')),
    path('home/', views.home, name='home'),
    path('bmi/', views.bmi, name='bmi'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('blogdetails/', views.blogdetails, name='blogdetails'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
     path('blog/', include('blog.URLS')),
     path('', include('authentication.urls')),
   
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
