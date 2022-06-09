from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .basket import Basket
from home.models import Product


def basket_add(request):
    basket = Basket(request)
    data = {}
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('product_quantity'))
        product = Product.objects.get(pk=product_id)
        basket.add(product=product, quantity=product_qty)
        data.update({'qty': basket.__len__(), 'basket_total': basket.elements_sum(), 'element_id': product_id})
    return JsonResponse(data, status=200)


def basket_page(request):
    return render(request, 'basket/basket.html')


def basket_delete(request):
    basket = Basket(request)
    data = {}
    if request.POST.get('action') == 'post':
        product_id = str(request.POST.get('productid'))
        print(basket.basket[product_id])
        print(basket.elements_sum())
        basket.delete(product_id)
        basket.save()
        data.update({'product': product_id, 'basket_total': basket.elements_sum(), 'basket_qty': basket.__len__()})
        return JsonResponse(data, status=200)
