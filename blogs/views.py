from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, BlogPost
from .forms import BlogForm, PostForm

def check_blog_owner(blog, request):
    """Page will not load if the user does not own the blog."""
    if blog.owner != request.user:
        raise Http404

def index(request):
    # Home page for blogs.
    return render(request, 'blogs/index.html')

def blogs(request):
    # Shows all created blogs.
    blogs = Blog.objects.order_by('date_created')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blogposts(request, blog_id):
    # Shows all the posts created by a blog.
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.order_by('-date_created')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blogposts.html', context)

@login_required
def new_blog(request):
    # Allows user to create a new blog.
    if request.method != 'POST':
        # No input given, create new blog form.
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blogs')
    
    # Return a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_post(request, blog_id):
    # Allows users to create posts in their blogs.
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(blog, request)

    if request.method != 'POST':
        # No input given, create new blogpost form
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.save()
            return redirect('blogs:blogposts', blog_id=blog_id)

    # Display the blank or invalid form.
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    # Allows users to create posts in their blogs.
    blogpost = BlogPost.objects.get(id=post_id)
    blog = blogpost.blog
    check_blog_owner(blog, request)

    if request.method != 'POST':
        # No input given, create new blogpost form
        form = PostForm(instance=blogpost)
    else:
        form = PostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('blogs:blogposts', blog_id=blog.id)

    # Display the blank or invalid form.
    context = {'blogpost': blogpost, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

