from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

GATEWAY_URL = "http://api_gateway:3001"

@app.route("/", methods=["GET", "POST"])
def index():
    flights = []
    if request.method == "POST":
        origin = request.form["origin"]
        destination = request.form["destination"]
        travel_date = request.form["travel_date"]
        params = {"origin": origin, "destination": destination, "travel_date": travel_date}
        resp = requests.get(f"{GATEWAY_URL}/flights", params=params)
        flights = resp.json() if resp.status_code == 200 else []
    return render_template("index.html", flights=flights)
