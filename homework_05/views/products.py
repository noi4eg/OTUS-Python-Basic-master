from flask import Blueprint, render_template

products_app = Blueprint("products_app", __name__)

PRODUCTS = {
    1: "Laptop",
    2: "Mobile",
    3: "tablets",
}

@products_app.route("/")
def get_products():
    # return "<h1>Produts list</h1>"
    return render_template("/products/list.html", products=PRODUCTS)
    
@products_app.route("/add/")
def add_product():
    return "add product views"