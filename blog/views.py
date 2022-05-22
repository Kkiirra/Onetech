from django.shortcuts import render
from .models import Blog


def single_blog(request, slug_item):
    blog = Blog.objects.get(slug=slug_item)
    return render(request, 'blog/single_blog.html', {'blog': blog})
