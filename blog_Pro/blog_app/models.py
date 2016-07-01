from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PostBlog(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    author = models.CharField('full Name', max_length=60)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
