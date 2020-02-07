# Suche mit hilfe der PLZ (Zip-code) den Namen, die Windgeschwindigkeit und die prozentuale Bewölkung des Ortes.

import requests
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

api_url = 'https://api.openweathermap.org/data/2.5/weather'
APPID = '7e4787f0a589580089be1549ee37c3f9'

class ZipWeather(Resource):
    def get(self, zip):
        param = {
            'APPID':APPID,
            'units': 'metric',
            'zip': zip+',de'
        }

        r = requests.get(api_url, params = param)
        j = r.json()

        name = j['name']
        wspeed = j['wind']['speed']
        clouds = j['clouds']['all']

        return f"City: {name}, Windgeschwindigkeit: {wspeed}, Cloudiness: {clouds}", 200

api.add_resource(ZipWeather, '/<string:zip>')

if __name__ == '__main__':
    app.run(debug = True)
