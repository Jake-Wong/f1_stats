import requests
import json

# Returns a string to show the 'score' between two drivers in qualifying
def cmp_qualy_results(driver1, driver2, season):

    # Stores the first driver's results
    r = requests.get("https://ergast.com/api/f1/" + str(season) + "/drivers/" + driver1 + "/qualifying.json")
    driver1_races = json.loads(r.text)["MRData"]["RaceTable"]["Races"]

    # Stores the second driver's results
    r = requests.get("https://ergast.com/api/f1/" + str(season) + "/drivers/" + driver2 + "/qualifying.json")
    driver2_races = json.loads(r.text)["MRData"]["RaceTable"]["Races"]

    # Finds the positions that each driver qualified in
    driver1_results = []
    for race in driver1_races:
        driver1_results.append(int(race["QualifyingResults"][0]["position"]))
    driver2_results = []
    for race in driver2_races:
        driver2_results.append(int(race["QualifyingResults"][0]["position"]))

    # Assigns scores to each driver
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
