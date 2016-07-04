from django.shortcuts import render

from .models import PostBlog

# Create your views here.
def home_view(request):
	template = 'index.html'
	blogs = PostBlog.objects.all()
	context = {
	'title': 'Santosh Blog - Home',
	'blog_list': blogs
	}
	
	return render(request, template, context)

def blog_list_view(request):
	template = 'blog_list.html'
	context = {}
	return render(request, template, context)

def detail_view(request, id):	
	template = 'detail.html'
	blog = PostBlog.objects.get(id=id)
	context = {
	'title': 'Detail page- Blog',
	'blog': blog
	}
	return render(request, template, context)


def about_view(request):
	template = 'about.html'
	context = {}
	return render(request, template, context)

def contact_view(request):
	template = 'contact.html'
	context = {}
	return render(request, template, context)


