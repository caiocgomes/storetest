from flask import Flask, render_template
from flaskext.markdown import Markdown
from Pages import ProductPage, Home
from Products import allProducts
from Probabilities import Probability

app = Flask(__name__)
Markdown(app)
prob = Probability()

@app.route('/product/<int:pid>', methods = ['GET'])
def testPage(pid):
    prod = allProducts[pid-1]
    productPage = ProductPage(product = prod, renderer = render_template, probCalculator = prob.FindProbabilityBuy)
    return productPage.render()

@app.route('/')
def home():
    homeP = Home(renderer = render_template)
    return homeP.render()


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = False)
