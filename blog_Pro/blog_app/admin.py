from django.contrib import admin

# Register your models here.
from .models import PostBlog

class PostBlogAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'content'] 
    list_display = ['title', 'author', 'created', 'updated']
    list_display_links = ['created', 'updated']
    list_filter = ['author']
    search_fields = ['title', 'content']
    list_editable = ['title']
    ordering = ['author']
    list_select_related = True	

    #actions_on_top = False 
    #actions_on_bottom = False
	#actions_selection_counter =  True



    class Meta:
    	model = PostBlog
    

admin.site.register(PostBlog, PostBlogAdmin)
