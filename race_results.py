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

    return driver_names

# Returns a string to show the 'score' between two drivers in race results
def cmp_race_results(driver1, driver2, season):

    # Stores the first driver's results
    r = requests.get("https://ergast.com/api/f1/" + str(season) + "/drivers/" + str(driver1) + "/results.json")
    driver1_races = json.loads(r.text)["MRData"]["RaceTable"]["Races"]

    # Stores the second driver's results
    r = requests.get("https://ergast.com/api/f1/" + str(season) + "/drivers/" + str(driver2) + "/results.json")
    driver2_races = json.loads(r.text)["MRData"]["RaceTable"]["Races"]

    # Finds the positiions that each driver finished in
    driver1_results = []
    for race in driver1_races:
        driver1_results.append(int(race["Results"][0]["position"]))
    driver2_results = []
    for race in driver2_races:
        driver2_results.append(int(race["Results"][0]["position"]))

    # Compares the results to give a head-to-head score
    driver1_score = 0
    driver2_score = 0
    i = 0
    while i < len(driver1_results):
        print(str(driver1_results[i]) + " " + str(driver2_results[i]))
        if driver1_results[i] < driver2_results[i]:
            driver1_score += 1
        else:
            driver2_score += 1
        i += 1

    return driver1 + " " + str(driver1_score) + "-" + str(driver2_score) + " " + driver2
