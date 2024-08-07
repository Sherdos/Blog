from django.contrib import admin
from post.models import Post, Comment, Like
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
