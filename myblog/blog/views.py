from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# def home_page(request):
#     context = {
#         'posts': Post.objects.all(),
#         }
#     return render(request, 'blog/home_page.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home_page.html'
    context_object_name = 'posts'