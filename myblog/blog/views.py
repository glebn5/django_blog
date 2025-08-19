from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Post
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import requires_csrf_token

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
    
    def form_valid(self, form):
        messages.success(self.request, 'Your post have been created!')
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_update.html'
    slug_url_kwarg = 'post_slug'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        print(self.request.user)
        print(obj.author)
        if self.request.user != obj.author:
            messages.error(self.request, "You can't edit this post, because you aren't the author!")
            raise PermissionDenied("!")
        return obj
        
    
    def get_success_url(self, **kwargs):
        return reverse('post_page', kwargs={'post_slug': self.object.slug})
    
    def form_valid(self, form):
        messages.success(self.request, 'Your updates have been applied!')
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home_page')
    template_name = 'blog/post_delete.html'
    slug_url_kwarg = 'post_slug'

    def form_valid(self, form):
        messages.success(self.request, 'Your post have been deleted!')
        return super().form_valid(form)
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        print(self.request.user)
        print(obj.author)
        if self.request.user != obj.author:
            messages.error(self.request, "You can't edit this post, because you aren't the author!")
            raise PermissionDenied("!")
        return obj
    

@requires_csrf_token
def custom_403(request, exception):
    return render(request, 'errors/403.html', status=403)