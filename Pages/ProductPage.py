from Page import Page
from Products import allProducts, User
import operator
from numpy import log, exp

def merge(dicts):
    items = []
    for dic in dicts:
        items += dic.items()
    return dict(items)

class ProductPage(Page):
    def __init__(self, product = None, probCalculator = None, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)
        self.template = 'product.mkd'
        self.product = product
        self.probCalculator = probCalculator

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
                    expReturn = self.getExpectedReturn(self.product, rec, user, discount)
                    recd.update({'return': expReturn, 'printableRet': "{p:.8f}".format(p=expReturn), 'discount': int(100 * discount)})
                    recData.append(recd)
        return sorted(recData, key = operator.itemgetter('return'), reverse=True)

    def getExpectedReturn(self, prod, rec, user, discount = 0.05):
        feats = {'age': user.ageGroup, 'sex': user.sex, 'inc': user.incomeGroup, 'edu': user.education}
        buyProbability = 0.2 * self.probCalculator(feats, prod.prodid, rec.prodid, str(discount))
        return exp(buyProbability * log((prod.price / (1 - discount) + rec.price) * (1-discount)) + (1-buyProbability) * log(prod.price))
        #return buyProbability * ((prod.price / (1 - discount)+ rec.price) * (1-discount)) + (1-buyProbability) * (prod.price)
