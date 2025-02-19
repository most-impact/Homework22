from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDetailView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<int:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete')
]