import requests
import json
import datetime

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

# Takes in a driver's data and returns their full name
def format_name(driver_data):
    return driver_data["givenName"] + " " + driver_data["familyName"]

# Parses a lap time string into a time object
def parse_laptime(laptime):
    return datetime.datetime.strptime(laptime, "%M:%S.%f").time()

# Formats a time object into a string with the suitable laptime format
def format_time(time):
    return ("%d:%d.%d" % (time.minute, time.second, time.microsecond))[:-3]

# Finds the time difference between two given laptimes, returns a string
def find_diff(laptime1, laptime2):
    t2 = datetime.timedelta(minutes = laptime2.minute, seconds = laptime2.second, microseconds = laptime2.microsecond)
    t1 = datetime.timedelta(minutes = laptime1.minute, seconds = laptime1.second, microseconds = laptime1.microsecond)
    diff = t1 - t2

    # Formats the string
    if diff.total_seconds() >= 0:
        delta = "+%.3f" % (diff.total_seconds())
    else:
        delta = "%.3f" % (diff.total_seconds())
    return delta
