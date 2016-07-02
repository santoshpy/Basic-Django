from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PostBlog(models.Model):
    title = models.CharField(help_text='write beautiful title of your blog', max_length=140)
    image = models.ImageField(null=True, blank=True, upload_to='blog_images',)
    content = models.TextField(help_text='Write something you wish to write!')
    author = models.CharField(help_text='full Name', max_length=60)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title
    
