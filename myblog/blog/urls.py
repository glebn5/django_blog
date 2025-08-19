from django.urls import path
from .views import *


urlpatterns = [
    path('', PostListView.as_view(), name = 'home_page'),
    path('post/<slug:post_slug>/', PostDetailView.as_view(), name = 'post_page'),
    path('post_create/', PostCreateView.as_view(), name = 'create_a_post'),
    path('post_update/<slug:post_slug>/', PostUpdateView.as_view(), name = 'post_update'),
    path('post_delete/<slug:post_slug>/', PostDeleteView.as_view(), name = 'post_delete'),
]