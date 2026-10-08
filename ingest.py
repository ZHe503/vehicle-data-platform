import csv
from main import add_vehicle

with open("data/vehicles.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for car in reader:
        make = car["make"]
        model = car["model"]
        year = int(car["year"])
        power_hp = int(car["power_hp"])
        fuel_type = car["fuel_type"]

        add_vehicle(make, model, year, power_hp, fuel_type)