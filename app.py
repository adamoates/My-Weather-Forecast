from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "dd3dab53331602598aae8479f1233d43"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = []

    if request.method == "POST":
        cities = [city.strip() for city in request.form["city"].split(",")]
        for city in cities:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "imperial"  # or "metric"
            }

            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                weather_data.append({
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"].title(),
                    "humidity": data["main"]["humidity"],
                    "icon": data["weather"][0]["icon"]
                })
            else:
                weather_data.append({"error": f"City '{city}' not found. Please try again."})

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
