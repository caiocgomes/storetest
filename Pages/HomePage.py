from Page import Page
from Products import allProducts

class Home(Page):

    def __init__(self, *args, **kwargs):
        super(Home, self).__init__(*args, **kwargs)
        self.template = 'home.mkd'

    def getData(self):
        return {'products': allProducts}
