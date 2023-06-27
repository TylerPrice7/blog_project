"""Forms for the blog app."""
from django import forms

from .models import Blog, BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['text']
        labels = {'text':''}

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['text']
        labels = {'text':''}
        widget = {'text': forms.Textarea(attrs={'cols': 80})}