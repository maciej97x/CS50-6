from flask import Flask, render_template, request

app2 = Flask(__name__)


@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index2.html", placeholder=name)