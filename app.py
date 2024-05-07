import requests
from flask import Flask, render_template
from fonctions import *


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/livres", methods=("GET", "POST"))
def livres():
    datas = get_books()
    return render_template("livres.html", datas=datas)

if __name__ == " __main__":
    app.run()