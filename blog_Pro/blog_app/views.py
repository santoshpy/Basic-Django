from django.shortcuts import render

from .models import PostBlog

# Create your views here.
def home_view(request):
	instance = PostBlog.objects.all()
	context = {
	'blog_list': instance
	}
	template = 'home.html'
	return render(request, template, context)

