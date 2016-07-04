from django.contrib import admin

# Register your models here.
from .models import PostBlog

class PostBlogAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'content', 'image', 'publish'] 
    list_display = ['author','title', 'updated', 'publish']
    #list_display_links = ['updated']
    list_filter = ['author']
    search_fields = ['title', 'content']
    list_editable = ['title', 'publish']
    ordering = ['author']
    list_select_related = True	

    #actions_on_top = False 
    #actions_on_bottom = False
	#actions_selection_counter =  True



    class Meta:
    	model = PostBlog
    

admin.site.register(PostBlog, PostBlogAdmin)
