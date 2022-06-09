

class Recently_viewed:
    """
    A base Recently_viewed class, providing some default behaviors that can be inherited or overrided, as necessary.
    """
    def __init__(self, request):
        self.session = request.session
        recently = self.session.get('recently')
        if 'recently' not in request.session:
            recently = self.session['recently'] = {}
        self.recently = recently

    def add(self, product):
        """
        Adding and updating the users recently session data
        """
        product_id = str(product.id)
        if product_id not in self.recently:
            self.recently[product_id] = product_id

        print(self.recently)

        self.session.modified = True
