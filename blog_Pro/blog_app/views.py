from django.shortcuts import render

from .models import PostBlog

# Create your views here.
def home_view(request):
	context = {}
	template = 'home.html'
	return render(request, template, context)