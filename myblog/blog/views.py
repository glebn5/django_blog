from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views.generic.detail import DetailView

class PostListView(ListView):
    model = Post
    template_name = 'blog/home_page.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.object
        context['prev_post'] = Post.objects.filter(id__lt=obj.id).last()
        context['next_post'] = Post.objects.filter(id__gt=obj.id).first()
        return context
