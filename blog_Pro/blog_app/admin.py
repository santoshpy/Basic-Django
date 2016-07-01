from django.contrib import admin

# Register your models here.
from .models import PostBlog

class PostBlogAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'content'] 
    list_display=['title', 'content', 'created', 'updated']
    

    class Meta:
    	model = PostBlog
    

admin.site.register(PostBlog, PostBlogAdmin)
