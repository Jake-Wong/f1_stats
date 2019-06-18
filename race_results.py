import requests
import json

# Finds surnames of each driver in the given season
def get_names(year):
    r = requests.get("https://ergast.com/api/f1/" + str(year) + "/drivers.json")

    # Stores requested data in dictionary
    mrdata = json.loads(r.text)
    driver_data = mrdata["MRData"]["DriverTable"]["Drivers"]

    # Stores each driver's name in a list
    driver_names = []
    for driver in driver_data:
        driver_names.append(driver["driverId"])

    print(driver_names)
    return driver_names

input = input("Please enter a year: ")
get_names(input)
