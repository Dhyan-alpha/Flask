from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/template")
def template():
    return render_template("index.html")

@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name, r=2)

@app.route("/")
def slas():
    return render_template("index.html")

@app.route("/list")
def lst():
    return render_template("index.html", content=["Dhyan","Hetal","Girish"])

if __name__ == "__main__":
    app.run(debug=True)
