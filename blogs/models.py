from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    """Blueprint for a basic blog."""
    text = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns the name of the blog."""
        return self.text

class BlogPost(models.Model):
    """Basic blog post. Relates to a blog"""
    blog = models.ForeignKey(to=Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a simple representation of the blog post."""
        if len(self.text) > 50:
            return (f"{self.text[:50]}...")
        else:
            return f"{self.text}"
