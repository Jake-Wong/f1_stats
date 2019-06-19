import requests
import json

# Returns a dictionary containing the driver's full names in a given season
def get_names(year):

    # Stores each driver along with its data
    r = requests.get("https://ergast.com/api/f1/" + str(year) + "/drivers.json")
    entrants = json.loads(r.text)["MRData"]["DriverTable"]["Drivers"]

    # Creates a dictionary with the driverId as the key and the driver's full name as the value
    driver_names = {}
    for driver in entrants:
        driver_names[driver["driverId"]] = driver["givenName"] + " " + driver["familyName"]

    return driver_names
