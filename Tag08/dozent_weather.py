# https://openweathermap.org/appid
# https://openweathermap.org/current

import requests
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

api_url = 'https://api.openweathermap.org/data/2.5/weather'
APPID = '7e4787f0a589580089be1549ee37c3f9'
q = 'Berlin,de'
# https://api.openweathermap.org/data/2.5/weather?q=Berlin,deu&APPID=XXX
param = {
    'q' : q,
    'APPID' : APPID,
    'units' : 'metric'
}

class Weather(Resource):

    def get(self):
        r = requests.get(api_url, params = param)
        j = r.json()
        return f"temp: {j['main']['temp']}, {j['weather'][0]['description']}", 200

api.add_resource(Weather, '/')

if __name__ == '__main__':
    app.run(debug = True)
