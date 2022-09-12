"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask, render_template, request, url_for
from .views.products import products_app


app = Flask(__name__)

app.config.update(ENV="development",)

app.register_blueprint(products_app, url_prefix="/products")

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/eastereggs/")
def e():
    print_request()
    req_met = request.method
    req_path = request.path
    req_url = request.url
    
    return {
        "method": req_met,
        "path": req_path,
        "url": req_url,
        "args": request.args,
        }

def print_request():
    print("request:", request)
    print("request.args:", request.args)
    print("request.method:", request.method)
    print("request.path:", request.path)
    print("request url:", request.url)

if __name__ == "main":
    app.run(debug=True)
