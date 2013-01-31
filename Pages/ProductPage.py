from Page import Page
from Products import allProducts, User
import operator
from random import uniform

def merge(dicts):
    items = []
    for dic in dicts:
        items += dic.items()
    return dict(items)

class ProductPage(Page):
    def __init__(self, product = None, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)
        self.template = 'product.mkd'
        self.product = product

    def getData(self):
        user = User()
        prodData = self.product.toDict()
        recData = {'recData': self.getRecomendations(user)}
        usrData = user.toDict()
        return merge([recData, prodData, usrData])


    def getRecomendations(self, user):
        recData = []
        for rec in allProducts:
            if rec.prodid != self.product.prodid:
                for discount in [0.05, 0.10, 0.15]:
                    recd = rec.toDict()
                    expReturn = self.getExpectedReturn(self.product.prodid, rec.prodid, user, discount)
                    recd.update({'return': expReturn, 'printableRet': "{p:.2f}".format(p=expReturn), 'discount': int(100 * discount)})
                    recData.append(recd)
        return sorted(recData, key = operator.itemgetter('return'), reverse=True)[0:5]

    def getExpectedReturn(self, prid, recid, user, discount = 0.05):
        return uniform(0, 100)
