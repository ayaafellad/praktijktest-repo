from flask import Flask
from flask import request
from datetime import datetime
from flask.templating import render_template


microweb_app =Flask(__name__)

@microweb_app.route("/")
def main():
    return render_template("index.html" , datetime_now = datetime.datetime.now())

@microweb_app.route("/time")
def time():
    return render_template("time.html")

@microweb_app.route("/map")
def map():
    return render_template("map.html")

@microweb_app.route("/login")
def map():
    return render_template("login.html")

@microweb_app.route("/create")
def map():
    return render_template("create.html")

if __name__ == "__main__":
    microweb_app.run(host="0.0.0.0", port=8802) 
