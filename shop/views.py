from others.recently_viewed import Recently_viewed
from django.shortcuts import render, get_object_or_404
from home.models import Product
from django.core.paginator import Paginator
from home.models import Category, Brand
from others.recently_viewed import Recently_viewed


def shop_page(request):
    products = Product.objects.all()
    products_found = len(products)

    paginator = Paginator(products, 10)
    page = request.GET.get('page')

    recently = Recently_viewed(request)
    products_id = recently.recently.keys()
    recently_view = Product.objects.filter(id__in=products_id)

    products = paginator.get_page(page)
    context = {
        'products': products,
        'products_found': products_found,
        'recently_view': recently_view,
    }

    return render(request, 'shop/shop.html', context)


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)

    paginator = Paginator(products, 10)
    page = request.GET.get('page')

    products = paginator.get_page(page)
    context = {
        'products': products,
        'selected_category': category_slug.replace('-', ' & ').capitalize(),
        'products_found': len(products),
    }

    return render(request, 'shop/shop.html', context)


def brand_list(request, brand_slug):
    brand = get_object_or_404(Brand, slug=brand_slug)
    products = Product.objects.filter(brand=brand)

    paginator = Paginator(products, 10)
    page = request.GET.get('page')

    products = paginator.get_page(page)
    context = {
        'products': products,
        'selected_category': brand_slug.capitalize(),
        'products_found': len(products),
    }

    return render(request, 'shop/shop.html', context)


def singleproduct(request, product_slug):
    product = Product.objects.get(slug=product_slug)

    recently = Recently_viewed(request)
    recently.add(product)
    products_id = recently.recently.keys()

    recently_view = Product.objects.filter(id__in=products_id)

    context = {
        'product': product,
        'recently_view': recently_view,
    }
    return render(request, 'shop/singleproduct.html', context)
