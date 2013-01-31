from Page import Page

class ProductPage(Page):
    def __init__(self, product = None, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)
        self.template = 'product.mkd'
        self.product = 'prod'

    def getData(self):
        return {'productName': self.product.name,
                'productPrice': self.product.price}



