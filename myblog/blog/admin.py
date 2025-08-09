from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content_for_admin', 'created_at']
    list_display_links = ['title']
    list_filter = ['title']

admin.site.register(Post, PostAdmin)