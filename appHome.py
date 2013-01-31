from flask import Flask, render_template, request
from flaskext.markdown import Markdown
from Pages import ProductPage
from Products import nbPear

app = Flask(__name__)
Markdown(app)

@app.route('/', methods = ['GET'])
def testPage():
    productPage = ProductPage(product = nbPear, renderer = render_template)
    return productPage.render()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = False)
    print 'ready...'
