# from django.http import HttpResponse
# from django.shortcuts import render,redirect
# from django.contrib.auth import login,authenticate
# from django.contrib.auth.models import User
# from django.contrib import messages
# def login(request):
#       return render(request,"login.html")
# # def signin(request):
# #       return render(request,"authentication/signin.html")



# def signup(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         conpassword = request.POST.get('conpassword')

#         myuser = User.objects.create_user(username=username, email=email, password=password)
#         myuser.first_name = fname
#         myuser.last_name = lname
#         myuser.save()

#         messages.success(request, "Your account has been successfully created.")
#         return redirect('login')

#     return render(request, "signup.html")

     
# def signout(request):
#       pass
# from .forms import NewUserForm
# from django.contrib.auth import login
# from django.contrib import messages

# def signup(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("main:homepage")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="signup.html", context={"register_form":form})

from django.shortcuts import  render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    template_name ='templates\login.html'
    fields = '__all__'
    redirect_authenticated_user=False
    
    def get_success_url(self):
        return reverse_lazy('home')
    
# class RegisterPage(FormView):
#     template_name='templates\signup.html'
#     form_class=UserCreationForm
#     redirect_authenticated_user=True
#     success_url= reverse_lazy('login')
    
#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)

#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('home')
#         return super(RegisterPage, self).get(*args, **kwargs)

# class RegisterPage(FormView):
#     template_name='signup.html'
#     form_class=UserCreationForm
#     redirect_authenticated_user=True
#     success_url= reverse_lazy('home')
    
#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)

#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('signup')
#         return super(RegisterPage, self).get(*args, **kwargs)

class RegisterPage(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)