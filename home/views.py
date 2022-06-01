from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from blog.models import Blog
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from customuser.views import login_view


def add_delete_wishlist(request):
    if request.user.is_authenticated:
        product_id = request.POST.get('productid')
        print(product_id)
        product = get_object_or_404(Product, id=product_id)
        user_favorite = request.user.favorites.all()
        count_fav = len(user_favorite)
        if product not in user_favorite:
            request.user.favorites.add(product)
            count_fav += 1
        else:
            request.user.favorites.remove(product)
            count_fav -= 1
        return JsonResponse({'user_favorite': count_fav})
    else:
        return JsonResponse({'url': '/login/'}, status=404)


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
