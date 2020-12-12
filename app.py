from flask import Flask, request, redirect
from flask import render_template

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run()