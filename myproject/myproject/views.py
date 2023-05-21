from django.http import HttpResponse
from django.shortcuts import render



def home(request):
      return render(request,"index.html")
def bmi(request):
      return render(request,"bmi.html")
def about(request):
      return render(request,"about.html")
def services(request):
      return render(request,"services.html")
def blog(request):
      return render(request,"blog.html")
def blogdetails(request):
      return render(request,"blogdetails.html")
def gallery(request):
      return render(request,"gallery.html")
def contact(request):
      return render(request,"contact.html")

