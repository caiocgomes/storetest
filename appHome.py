from flask import Flask, render_template, request
from flaskext.markdown import Markdown
from Pages import ProductPage
from Products import allProducts

app = Flask(__name__)
Markdown(app)

@app.route('/product/<int:pid>', methods = ['GET'])
def testPage(pid):
    prod = allProducts[pid-1]
    productPage = ProductPage(product = prod, renderer = render_template)
    return productPage.render()

@app.route('/')
def home():
    return "fazer home"


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = False)
