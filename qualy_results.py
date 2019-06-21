import requests
import json
import driver_data

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

    print("QUALIFYING RESULTS:")

    # Assigns scores to each driver
    driver1_score = 0
    driver2_score = 0
    i = 0
    while i < len(driver1_results):
        print("P" + str(driver1_results[i]) + " P" + str(driver2_results[i]))
        if driver1_results[i] < driver2_results[i]:
            driver1_score += 1
        else:
            driver2_score += 1
        i += 1

    driver_names = driver_data.get_names(season)
    print(driver_names[driver1] + " " + str(driver1_score) + "-" + str(driver2_score) + " " + driver_names[driver2])

# Compares fastest qualifying times between drivers
def cmp_fastest_lap(driver1, driver2, season, round):

    # Stores the results of a qualifying session
    r = requests.get("https://ergast.com/api/f1/" + str(season) + "/"+ str(round) + "/qualifying.json")
    quali_results = json.loads(r.text)["MRData"]["RaceTable"]["Races"][0]["QualifyingResults"]

    # Gets the driver's best times
    for driver in quali_results:
        if driver["Driver"]["driverId"] == driver1:
            driver1_name = driver["Driver"]["givenName"] + " " + driver["Driver"]["familyName"]
            driver1_pos = "P" + driver["position"]
            # Finds the fastest lap for driver1
            if "Q3" in driver:
                driver1_time = driver_data.parse_laptime(driver["Q3"])
            elif "Q2" in driver:
                driver1_time = driver_data.parse_laptime(driver["Q2"])
            else:
                driver1_time = driver_data.parse_laptime(driver["Q1"])
        elif driver["Driver"]["driverId"] == driver2:
            driver2_name = driver["Driver"]["givenName"] + " " + driver["Driver"]["familyName"]
            driver2_pos = "P" + driver["position"]
            # Finds the fastest lap for driver2
            if "Q3" in driver:
                driver2_time = driver_data.parse_laptime(driver["Q3"])
            elif "Q2" in driver:
                driver2_time = driver_data.parse_laptime(driver["Q2"])
            else:
                driver2_time = driver_data.parse_laptime(driver["Q1"])

    # Finds the time difference between driver 1's best time and driver 2's best time
    lap_diff = driver_data.find_diff(driver1_time, driver2_time)
    print(driver1_pos + " " + driver1_name + " " + driver_data.format_time(driver1_time) + "\n" + lap_diff + "\n" + driver2_pos + " " + driver2_name + " " + driver_data.format_time(driver2_time))
