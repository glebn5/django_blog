from django.urls import path
from .views import PostListView, PostDetailView


urlpatterns = [
    path('home/', PostListView.as_view(), name = 'home_page'),
    path('post/<slug:post_slug>/', PostDetailView.as_view(), name = 'post_page'),
]