# create a web server using flask and python

from flask import Flask as f

app = f(__name__)

@app.route("/")
def hello_world():
    return"<h1>Hello World</h1>"

app.run()# used to run this program

