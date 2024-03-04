import json
import time
import random

# Création de la liste pour stocker les données
sensor_data = []

# Ajout du capteur de température
temperature_sensors = {"name": "temperature sensor", "unit": "Celsius", "readings": []}

# Ajout du capteur de de qualité d'air
air_quality_sensors = {"name": "air quality sensor", "unit": "2.5 PM", "readings": []}




# Lecture du capteur de température
def read_temperature_sensor():
    return random.randint(21, 25)

# Lecture du capteur de température
def read_air_quality_sensor():
    return round(random.uniform(12.0, 14.5), 1)



# Lecture des capteurs simultanément, répétée 5 fois
for _ in range(5):
    current_time = time.gmtime()

    iteration_data = {
        "id": _ + 1,
        "temperature": {
            "time": {
                "hour": current_time.tm_hour,
                "minute": current_time.tm_min,
                "second": current_time.tm_sec,
            },
            "value": read_temperature_sensor(),
        },
        "air_quality": {
            "time": {
                "hour": current_time.tm_hour,
                "minute": current_time.tm_min,
                "second": current_time.tm_sec,
            },
            "value": read_air_quality_sensor(),
        },
    }

    # Ajout des données de l'itération à la liste des données des capteurs
    sensor_data.append(iteration_data)

# Convertir la liste en une chaîne JSON
json_data = json.dumps(sensor_data, indent=5, separators=("}, ", ": "))

# Write the JSON string to a file
with open("sensor_readings.json", "w") as f:
    f.write(json_data)
    
# Imprimer les données JSON
print(json_data)

