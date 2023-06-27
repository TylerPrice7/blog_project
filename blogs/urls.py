"""Defines URL paths for blogs"""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Shows all blogs.
    path('blogs/', views.blogs, name="blogs"),
    # Shows all the blog posts for a blog.
    path('blogs/<int:blog_id>/', views.blogposts, name="blogposts"),
    # Page for creating a new blog.
    path('new_blog/', views.new_blog, name='new_blog'),
    # Path for creating new blog posts.
    path('new_post/<int:blog_id>/', views.new_post, name='new_post'),
    # Path for editing past blog posts.
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]