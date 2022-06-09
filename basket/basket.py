from home.models import Product


class Basket:
    """
    A base Basket class, providing some default behaviors that can be inherited or overrided, as necessary.
    """
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, quantity):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.product_cost), 'qty': int(quantity)}
        else:
            self.basket[product_id]['qty'] += quantity

        self.session.modified = True

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())

    def elements_sum(self):
        return sum(float(item['price']) * item['qty'] for item in self.basket.values())

    def __iter__(self):
        products_ids = self.basket.keys()
        products = Product.objects.filter(id__in=products_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = product

        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def save(self):
        self.session.modified = True
