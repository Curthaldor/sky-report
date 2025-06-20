from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

def fetch_kp_index():
    url = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"
    response = requests.get(url)
    data = response.json()
    latest = data[-1]

    return {
        "time": latest["time_tag"],
        "kp_index": latest["kp_index"],
        "estimated_kp": latest["estimated_kp"],
        "kp_label": latest["kp"]
    }

@app.route("/")
def index():
    kp_data = fetch_kp_index()
    return render_template("index.html", kp=kp_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
