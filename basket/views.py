from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .basket import Basket
from home.models import Product


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('product_quantity'))
        product = Product.objects.get(pk=product_id)
        basket.add(product=product, quantity=product_qty)
    return JsonResponse({'qty': basket.__len__(), 'basket_total': basket.elements_sum()})
