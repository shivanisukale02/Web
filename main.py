from flask import Flask
app=Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome To my Website"

@app.route("/contact")
def ContactPage():
    return "Contact page"

@app.route("/Home")
def Home():
    return "Home Page"

@app.route("/Gallary")
def Gallary():
    return "Here is gallary"

if __name__=="__main__":
    app.run()

