from .basket import Basket


def basket(request):
    basket_cart = Basket(request)
    return {'basket': basket_cart, 'basket_qty': basket_cart.__len__(), 'basket_sum': basket_cart.elements_sum()}
