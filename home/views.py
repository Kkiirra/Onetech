from django.db.models import Q
from blog.models import Blog
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def categories(request):
    return {
        'categories': Category.objects.order_by('name')
    }


def home_page(request):
    products = Product.objects.all()[:16]
    week_deals = Product.objects.filter(full_hd_image__isnull=False)
    blogs = Blog.objects.order_by('date')
    new_products = Product.objects.filter(new=True)
    top_sellers = Product.objects.filter(Q(product_cost__lt=700) | Q(sold__gt=0))
    trends = Product.objects.filter(trends=True)
    full_screen_iphone = Product.objects.get(product_name='Apple Iphone 13s')
    full_screen_macbook = Product.objects.get(product_name='MacBook Air 13')

    context = {
        'products': products, 'deals': week_deals, 'new_products': new_products, 'top_sellers': top_sellers,
        'trends': trends, 'full_screen_preview': full_screen_iphone, 'full_screen_macbook': full_screen_macbook,
        'blogs': blogs
    }

    return render(request, 'home/home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, '#', {'product': product})


def search_product(request):
    user_request = request.GET.get('search')
    products = Product.objects.filter(product_name__icontains=user_request)
    return render(request, 'shop/shop.html', {'products': products, 'products_found': len(products)})
