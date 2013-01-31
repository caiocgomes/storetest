import MySQLdb as mdb
from cacheable import cache

alpha = 0.1
beta  = 1.0

class Probability(object):

    def __init__(self):
        self.conn = mdb.connect('cpbigdata.c3bofhlifl67.sa-east-1.rds.amazonaws.com','root','mula1777-','recomendation')
        self.cursor = self.conn.cursor()

    def FindProbabilityBuy(self,features,product,recom,discount):
        probFeature={}
        for feature in features:
            countFeatures = {'0': self.FindProbabilityFeature(feature,features[feature],product,recom,discount,0),
                             '1': self.FindProbabilityFeature(feature,features[feature],product,recom,discount,1)}

            countTotal = {'0':self.FindProbabilityTotal(product,recom,discount,0),
                          '1':self.FindProbabilityTotal(product,recom,discount,1)}

            probFeature[feature] = {'0': (alpha + countFeatures['0'])/(alpha + beta + countTotal['0']),
                                    '1': (alpha + countFeatures['1'])/(alpha + beta + countTotal['1'])}

        c = 1
        for feature in features:
            c = c * probFeature[feature]['0']/probFeature[feature]['1']

        countT = countTotal['0'] + countTotal['1']
        probTotal = {'0':(alpha + countTotal['0'])/(alpha + beta + countT),'1':(alpha + countTotal['1'])/(alpha + beta + countT)}
        d = c * probTotal['0']/probTotal['1'] + 1
        return 1.0 / d

    def FindProbabilityFeature(self,feature,featValue,product,recom,discount,compra):
        query = "SELECT count from recomendation.features where featName = \'{featname}\' and featValue = \'{featValue}\' and discount = \'{discount}\' and prod = {product} and rec = {rec} and compra = {compra}".format(featValue=featValue,discount=discount,featname=feature,product=product,rec=recom,compra= compra)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return float(result[0][0]) if len(result)> 0 else 0.0

    @cache
    def FindProbabilityTotal(self,product,recom,discount,compra):
        query = "SELECT count from recomendation.totals where  prod = {product} and rec = {rec} and compra={compra} and discount={discount}".format(product=product,rec=recom,compra=compra,discount=discount)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return float(result[0][0]) if len(result) > 0 else 0.0

prob = Probability()

for i in xrange(1,22):
    for j in xrange(1, 22):
        #print prob.FindProbabilityTotal(i, j, '0.15', 0)
        #print prob.FindProbabilityTotal(i, j, '0.15', 1)
        #print prob.FindProbabilityFeature('sex', 'F', i, j, '0.15', 0)
        #print prob.FindProbabilityFeature('sex', 'F', i, j, '0.15', 1)
        print  i, j, prob.FindProbabilityBuy({'sex': 'M', 'age':1, 'inc':1, 'edu':1}, i, j, '0.15')
