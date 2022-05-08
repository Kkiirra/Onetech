from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def categories(request):
    return {
        'categories': Category.objects.order_by('name')
    }


def home_page(request):
    products = Product.objects.all()[:16]

    week_deals = Product.objects.filter(full_hd_image__isnull=False)
    new_products = Product.objects.filter(new=True)
    top_sellers = Product.objects.filter(product_cost__lt=300)
    trends = Product.objects.filter(trends=True)

    full_screen_iphone = Product.objects.get(product_name='Apple Iphone 13s')
    full_screen_macbook = Product.objects.get(product_name='MacBook Air 13')

    context = {
        'products': products, 'deals': week_deals, 'new_products': new_products, 'top_sellers': top_sellers,
        'trends': trends, 'full_screen_preview': full_screen_iphone, 'full_screen_macbook': full_screen_macbook,
    }

    return render(request, 'home/home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, '#', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return HttpResponse(f'Nice {products[0].product_name}')
