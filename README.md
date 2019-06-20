# F1 Statistics
A program that compares the performance between drivers in a given season using data from the Ergast Developer API.
This is just a small summer project to allow me to teach myself and experiment with python

### Race results
The program can compare the race results between two selected drivers for a given season. For example, if I was to compare Max Verstappen with Charles Leclerc the cmp_race_results() function would return "max_verstappen 5-2 leclerc" along with a list of their finishing positions repectively (As of the 2019 Canadian GP).

### Qualifying results
Similar to race results, the qualifying results between two drivers for a given season can also be compared to return a score. The cmp_qualy_results() function operates in a way similar to its race result counterpart meaning that it would return a string "norris 4-3 sainz" with a list of their qualifying positions (As of the 2019 Canadian GP).
Furthermore, the time delta between the fastest qualifying laps of drivers can be compared. The function cmp_fastest_lap() finds the fastest lap set by the two selected drivers, displays their respective times along with the time difference between the laps.
