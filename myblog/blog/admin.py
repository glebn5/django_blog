from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content_for_admin', 'author','created_at']
    list_display_links = ['title']
    list_filter = ['title']
    prepopulated_fields = {"slug": ["title"]}

admin.site.register(Post, PostAdmin)