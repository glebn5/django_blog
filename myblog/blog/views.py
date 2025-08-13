from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Post
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

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
        context['prev_post'] = Post.objects.filter(id__lt=obj.id).first()
        context['next_post'] = Post.objects.filter(id__gt=obj.id).last()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    template_name = 'blog/post_create.html'

    def get_success_url(self, **kwargs):
        return reverse('post_page', kwargs={'post_slug': self.object.slug})

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_update.html'
    slug_url_kwarg = 'post_slug'
    
    def get_success_url(self, **kwargs):
        return reverse('post_page', kwargs={'post_slug': self.object.slug})

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home_page')
    template_name = 'blog/post_delete.html'
    slug_url_kwarg = 'post_slug'