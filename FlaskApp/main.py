from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, Python World!</h1>"


@app.route("/products")
def products():
    return "<h1>This is the Product page</h1>"


@app.route("/orders")
def orders():
    return "<h1>This is the Orders page</h1>"


@app.route("/order/<orderID>")
def order(orderID):
    return 'This is the Order page with {}'.format(orderID)
