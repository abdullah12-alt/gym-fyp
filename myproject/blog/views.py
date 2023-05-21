from django.shortcuts import render
from django.views import generic
from .models import blog
# Create your views here.
class blogList(generic.ListView):
    queryset = blog.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class blogDetails(generic.DetailView):
    model = blog
    template_name = 'blogdetails.html'