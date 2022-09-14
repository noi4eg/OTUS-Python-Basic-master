from flask import Flask, render_template, request, url_for, jsonify
from werkzeug.exceptions import BadRequest, NotFound
from werkzeug.utils import redirect

# flask --app .\homework_05\app.py run --debugger --reload

app = Flask(__name__)

PRODUCTS = {
    1: "Mobile",
    2: "PC",
    3: "Xbox",
}

@app.route("/")
def root():
    return render_template("base.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/prods_list/", endpoint="prods_list")
def prods_list():
    return render_template("list.html", prods=list(PRODUCTS.items()))

@app.route("/<int:prod_id>/", endpoint="prod_details")
def get_prod_by_id(prod_id: int):
    try:
        prod_name = PRODUCTS[prod_id]
    except KeyError:
        raise NotFound(f"Prod #{prod_id} not found!")

    return render_template(
        "details.html",
        prod_id=prod_id,
        prod_name=prod_name,
    )



@app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_prod():
    if request.method == "GET":
        return render_template("add_prod.html")

    prod_name = request.form.get("prod-name")
    if not prod_name:
        raise BadRequest("Prod name is required, please fill `prod-name`")

    prod_id = len(PRODUCTS) + 1
    PRODUCTS[prod_id] = prod_name

    prod_url = url_for("prod_details", prod_id=prod_id)
    return redirect(prod_url)