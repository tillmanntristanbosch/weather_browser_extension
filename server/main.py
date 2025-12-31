import json
import requests
from flask import Flask
from flask_cors import CORS  # <-- NEU: Importieren

app = Flask(__name__)
CORS(app)  # <-- NEU: CORS für alle Routes erlauben (oder spezifisch: CORS(app, origins=["moz-extension://*"]))

# Wettercodes laden (pfad ggf. anpassen)
weathercodes = json.load(open("weathercodes.json", "r", encoding="utf-8"))

lat, lon = 49.4621020310017, 8.47714801139806

@app.route('/t')
def get_temp():
    try:
        response = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
        )
        response.raise_for_status()
        temp = response.json()["current"]["temperature_2m"]

        if temp > 20:
            text = f"Das Wetter heute beträgt schöne {temp} Grad Celsius"
        else:
            text = f"Das Wetter heute beträgt leider recht kalte {temp} Grad Celsius :("
        return text, 200
    except Exception as e:
        return f"Fehler bei der Abfrage: {str(e)}", 500

@app.route('/w')
def get_weather():
    try:
        response = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,windspeed_10m,weathercode"
        )
        response.raise_for_status()
        data = response.json()
        weathercode = data["current"]["weathercode"]
        text = weathercodes.get(str(weathercode), "Unbekannter Wettercode")
        return text, 200
    except Exception as e:
        return f"Fehler bei der Abfrage: {str(e)}", 500

@app.route('/')
def index():
    return """
    <h1>Wetter-Server läuft</h1>
    <p>Verfügbare Endpoints:</p>
    <ul>
        <li><a href="/t">/t</a> → Temperatur</li>
        <li><a href="/w">/w</a> → Wetterbeschreibung</li>
    </ul>
    """

if __name__ == '__main__':
    print("Wetter-Server startet auf http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=True)