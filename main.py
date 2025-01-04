from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask("YojanaMitra")

@app.route("/")
def home():
    return render_template("dashboard/dashboard.html")

@app.route("/schemes")
def schemes():
    return render_template("dashboard/schemes.html")

@app.route("/schemes/support_for_value_addition")
def scheme():
    return render_template("schemes/scheme.html")

if __name__ == "__main__":
    app.run(debug=True)