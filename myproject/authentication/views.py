from django.shortcuts import redirect
from django.contrib import auth
from django.views.decorators.cache import cache_control
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .forms import  *
from .models import *
from .utils import  *


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    auth.logout(request)
    request.session.flush()  # Clear session data
    return redirect('home')

class CustomLoginView(LoginView):
    template_name ='templates/login.html'
    fields = '__all__'
    redirect_authenticated_user = False
    
    def get_success_url(self):
        return reverse_lazy('home')

    def logout_view(request):
        auth.logout(request)
        request.session.flush()  # Clear session data
        return redirect('home')

class RegisterPage(FormView):
    template_name='signup.html'
    form_class= UserCreationForm
    redirect_authenticated_user=True
    success_url= reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)
