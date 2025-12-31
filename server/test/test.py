import requests
import json

weathercodes = json.load(open("weathercodes.json", "r", encoding="utf-8"))
lat, lon = 49.4621020310017, 8.47714801139806

while True:
    inp = input("t for temp, w for weather, stop to exit: ")

    if inp == "t":
        temp = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m").json()["current"]["temperature_2m"]
        if temp > 20:
            print (f"Das wetter heute beträgt schöne {temp} Grad Celsius")
        elif temp < 20:
            print (f"Das wetter heute beträgt leider recht kalte {temp} Grad Celsius :(")

    elif inp == "w":
        weather = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,windspeed_10m,weathercode")
        data = weather.json()
        current = data["current"]
        weathercode = current["weathercode"]
        print(weathercodes[str(weathercode)])

    elif inp == "stop":
        break
    
    else:
        print("Kein gültiger Befehl.")
