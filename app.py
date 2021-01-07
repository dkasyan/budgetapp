from flask import Flask, request, redirect
from flask import render_template
from main import get_mesure
from forms import Dashboard

app = Flask(__name__)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    dash = Dashboard()
    dash.humidity = "Dks"
    dash.temperature = "dwa"

      
        
    return render_template("dashboard.html", dash=dash)


if __name__ == '__main__':
    app.run(debug=True)