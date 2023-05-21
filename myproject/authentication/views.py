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
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conpassword = request.POST.get('conpassword')

        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your account has been successfully created.")
        return redirect('login')

    return render(request, "signup.html")

     
def signout(request):
      pass
