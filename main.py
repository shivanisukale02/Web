import flask
from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def Welcome():
    return "<h1>Welcome</h1>"

@app.route("/contact")
def ContactPage():
    return render_template("Contact.html")

@app.route("/Home")
def Home():
    return "Home Page"

@app.route("/Gallary")
def Gallary():
    return "Here is gallary"

if __name__=="__main__":
    app.run()

