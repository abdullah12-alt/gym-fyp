from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
def login(request):
      return render(request,"login.html")
# def signin(request):
#       return render(request,"authentication/signin.html")

def signup(request):
     if request.method == "POST":
      username =request.POST('username')      
      fname =request.POST('fname')      
      lname =request.POST('lname')      
      email =request.POST('email')      
      password =request.POST('password')      
      conpassword =request.POST('conpassword') 

      myuser = User.objects.create_user( username, email, password )
      myuser.first_name = fname     
      myuser.last_name = lname 
      myuser.save()
      messages.success(request , "Your Account has been successfully created.")
      return redirect('login')  
      
      return render(request,"signup.html")
     
def signout(request):
      pass
