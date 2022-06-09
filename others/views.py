from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from home.models import Product
from .recently_viewed import Recently_viewed


def recently_viewed(request):
    recently = Recently_viewed(request)
    item = 7
    product = Product.objects.filter(pk=item)[0]
    recently.add(product)
    ids = recently.recently.keys()
    products = Product.objects.filter(id__in=ids)
    return redirect('home:home_page')


def add_delete_wishlist(request):
    if request.user.is_authenticated:
        product_id = request.POST.get('productid')
        product = get_object_or_404(Product, id=product_id)
        print(product)
        user_favorite = request.user.favorites.all()
        count_fav = len(user_favorite)

        if product not in user_favorite:
            request.user.favorites.add(product)
            count_fav += 1
        else:
            request.user.favorites.remove(product)
            count_fav -= 1
        return JsonResponse({'user_favorite': count_fav}, status=200)
    else:
        return JsonResponse({'url': '/login/'}, status=404)
