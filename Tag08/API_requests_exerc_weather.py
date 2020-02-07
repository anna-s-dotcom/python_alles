import requests
import json
from flask import Flask,request

app = Flask(__name__)


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    apikey = "d0febed86e177ba351c599032d1d624c"
    params = {
        "q":city,
        "units":"metric",
        "APPID":apikey,
        "lang":"de"
    }
    req = requests.get(url,params=params)
    weather_dict = json.loads(req.text)
    current_temp = weather_dict["main"]["temp"]
    current_weather = weather_dict["weather"][0]["description"]
    return (current_temp,current_weather)

@app.route("/",methods=["POST","GET"])
def index():
    city = "Berlin"
    if request.method == "POST":
        city = request.form.get("city")
    try:    
        current_temp, current_weather = get_weather(city)
        return f""" <div style="text-align:center;margin:100px">
                    <p><form method="post">
                        <input type="text" name="city" placeholder="Stadt" style="font-size:20px;height:auto">
                        <input type="submit" name="submit" value="Anfragen" style="font-size:20px;height:auto">
                        </form>
                    </p>
                    <p style="font-size:30px">Aktuelles Wetter in {city}:</p>
                    <p style="font-size:25px">{current_weather} bei {current_temp} °C</p></div>"""
    except KeyError:
        return  f"""<div style="text-align:center;margin:100px">
                    <p><form method="post">
                        <input type="text" name="city" placeholder="Stadt" style="font-size:20px;height:auto">
                        <input type="submit" name="submit" value="Anfragen" style="font-size:20px;height:auto">
                        </form>
                    </p>
                    <p style="font-size:30px">Kein Ergebnis für Suchbegriff {city}.</p>"""

if __name__ == "__main__":
    app.run(debug=True)