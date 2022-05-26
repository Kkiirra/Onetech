from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .basket import Basket


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('productid')
        print(product_id)
    return JsonResponse({'data': 'test'})
