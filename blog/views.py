from django.shortcuts import render
from .models import Blog


def single_blog(request, slug_item):
    blog = Blog.objects.get(slug=slug_item)
    return render(request, 'blog/single_blog.html', {'blog': blog})


def blogs_page(request):
    blogs = Blog.objects.order_by('date')[:9]
    return render(request, 'blog/blog.html', {'blogs': blogs})
