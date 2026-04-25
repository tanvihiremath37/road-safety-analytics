"""
Synthetic Road Accident Dataset Generator
Saves dataset to: Data/road_accidents.csv
"""

import pandas as pd
import random
import os
from datetime import datetime, timedelta

# Reproducibility
random.seed(42)

# ===== FILE PATH SETUP =====
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "Data", "road_accidents.csv")

# ===== DATA CONFIG =====
city_coords = {
    "Bangalore": (12.9716, 77.5946),
    "Mumbai": (19.0760, 72.8777),
    "Delhi": (28.7041, 77.1025),
    "Chennai": (13.0827, 80.2707)
}

areas = ["Urban", "Rural", "Highway"]
vehicles = ["Car", "Bike", "Truck", "Bus"]
road_conditions = ["Dry", "Wet", "Damaged"]

# ===== HELPER FUNCTIONS =====
def get_light(hour):
    return "Night" if hour < 6 or hour > 18 else "Day"

def get_severity(light, road, vehicle, area):
    score = 0
    
    if light == "Night":
        score += 2
    if road == "Wet":
        score += 2
    if road == "Damaged":
        score += 1
    if vehicle == "Bike":
        score += 1
    if vehicle == "Truck":
        score += 1
    if area == "Highway":
        score += 2

    if score >= 5:
        return "Fatal"
    elif score >= 3:
        return "Serious"
    else:
        return "Minor"

def get_location(city):
    base_lat, base_lon = city_coords[city]
    
    lat = base_lat + random.uniform(-0.05, 0.05)
    lon = base_lon + random.uniform(-0.05, 0.05)
    
    return round(lat, 6), round(lon, 6)

# ===== DATA GENERATION =====
data = []
start_date = datetime(2024, 1, 1)

for i in range(5000):
    date = start_date + timedelta(days=random.randint(0, 365))
    
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    time = f"{hour:02d}:{minute:02d}"
    
    city = random.choice(list(city_coords.keys()))
    area = random.choice(areas)
    vehicle = random.choice(vehicles)
    road = random.choice(road_conditions)
    light = get_light(hour)
    
    vehicles_count = random.randint(1, 4)
    severity = get_severity(light, road, vehicle, area)
    
    lat, lon = get_location(city)
    weekday = date.strftime("%A")

    data.append([
        i,
        date.date(),
        time,
        weekday,
        city,
        area,
        vehicle,
        road,
        light,
        vehicles_count,
        severity,
        lat,
        lon
    ])

# ===== CREATE DATAFRAME =====
df = pd.DataFrame(data, columns=[
    "accident_id",
    "date",
    "time",
    "weekday",
    "city",
    "area_type",
    "vehicle_type",
    "road_condition",
    "light_condition",
    "vehicles_involved",
    "severity",
    "latitude",
    "longitude"
])

# ===== SAVE FILE =====
df.to_csv(file_path, index=False)

print("Dataset created successfully!")
print("Saved at:", file_path)
print(df.head())