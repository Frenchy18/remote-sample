"""
    Module for displaying information about meteor data from the NASA Meteorite Landings dataset:
    https://data.nasa.gov/widgets/gh4g-9sfh

    Created by: Vincent Baccari & Christopher Groves
"""
import sys
import csv
import math
from math import radians, cos, sin, sqrt, atan2, asin

# Constants for specific columns in the csv
METEOR_NAME = 0
METEOR_ID = 1
METEOR_NAMETYPE = 2
METEOR_RECCLASS = 3
METEOR_MASS = 4
METEOR_FALL = 5
METEOR_YEAR = 6
METEOR_LAT = 7
METEOR_LON = 8
YEAR_RANGE = range(0,3000)
MAX_LAT = 90
MAX_LON = 180

def load_data():
    """Load meteorite data into a "list of lists".
    Each element in the list corresponds to a single line in the CSV file.
    Each line has 9 elements: name,id,nametype,recclass,mass (g),fall,year,reclat,reclong

    Returns:
        list: a list of lists, where each inner list contains the data for one meteor
    """
    # Vincent implemented the try, except block
    try:
        with open('Lab3/meteorite_landings_full.csv', encoding='utf-8', newline='') as csvfile:
            next(csvfile)  # skip the header row
            return list(csv.reader(csvfile))
    except FileNotFoundError:
        raise FileNotFoundError("File not found. Check file path and try again.")
    except Exception as e:
        raise Exception(f"Error loading the file: {e}")


def main():
    """The main function that provides the console interface for the application.
    """
    # attempt to get the command and argument from the CLI or the input() console.
    result = None
    # Read the CSV file data into a list.
    try:
        meteors = load_data()
        print("File input valid")
    except Exception as e:
        print(e)
        return

    if len(sys.argv) == 3:
        command = sys.argv[1]
        arg = sys.argv[2]
    else:
        print("Give a command. Options are:")
        print("1. Search by year, input year <year>")
        print("2. Search by latitude and longitude, input geopoint <latitude>,<longitude>")
        print("3. Search by the recclass, input recclass <class>")
        print("4. Find the heaviest meteor, heaviest <number of meteors>")
        print("5. Search for each Fall category and output how many each has, count-class")

        user_input = input("Enter a command: ").strip().split(' ',1)
        command = user_input[0]
        if len(user_input) > 1:
            arg = user_input[1]
        else:
            arg = None

        


    # Add code here to validate command & arg, and then call the functions to process the data.
    # Validates command and arg, then calls the function

    # Chris put together the majority of the validation and Vincent pointed out
    # occasional flaws in logic and fixed a neverending loop Chris accidentally put in.
    if command == '1' or command == 'year':
        try:
            result = year(meteors, arg)
        except Exception as e:
            print(e)
            
    elif command == '2' or command == 'geopoint':
        try:
            lat,lon = arg.strip().split(',')
            if float(lat) and float(lon):
                result = geo_point(meteors,lat,lon)
        except ValueError as e:
            print("Invalid geopoint format. Requires '<latitude>,<longitude>'.",e)
        except UnboundLocalError:
            print(f"{arg} is not valid input. Please enter valid <latitude>,<longitude>.")
    
    elif command == '3' or command == 'recclass':
        result = find_reclass(meteors, arg)
        
    elif command == '4' or command == 'heaviest':
        result = high_mass(meteors,arg)     
        
    elif command == '5' or command == 'count-class':
        result = count_class(meteors)
    else:
        raise ValueError("Incorrect input. Please enter 'year', 'geopoint', 'recclass', 'heaviest', or 'count-class'.")

    # Outputs the result
    if result:
        print(result)

# Vincent primarily implemented the year function
def year(meteors, year):
    """Returns meteor sightings for the designated year.

    Args:
        meteors (list): Ordered list of meteor sightings
        year (int): Valid input year from user

    Returns:
        str: A formatted string of result or message indicating no meteors were found.
    """
    
    if not isinstance(year,str):
        raise ValueError(f"{year} is invalid. Please enter a valid 4 digit year.")
    if not year.isdigit() or len(year) != 4:
        raise ValueError(f"{year} is invalid. Please enter a valid 4 digit year.")
    
    year = int(year)
    if year not in YEAR_RANGE:
        raise IndexError(f"{year} not within valid range.")
    
    result = []
    for i in meteors:
        if i[METEOR_YEAR] == str(year):
            if i[METEOR_LAT] and i[METEOR_LON]:
                result.append(f'The meteor {i[METEOR_NAME]} ID: {i[METEOR_ID]} Type: {i[METEOR_NAMETYPE]} Recclass: {i[METEOR_RECCLASS]} Mass (g): {i[METEOR_MASS]} fall type: {i[METEOR_FALL]} landed at {i[METEOR_LAT]} and {i[METEOR_LON]}.')

    if result:
        return '\n'.join(result)
    return (f"No meteors found for the year {year}")

# Vincent implemented the recclass function
def find_reclass(meteors, recclass):
    """ Searches through the meteor list and finds all instances that contain the recclass matching the user input

    Args:
        meteors (_list_): Ordered list of meteor sightings
        recclass (_string_): Recclass type being searched for by the user

    Returns:
        _String_: List of meteors appended to result or message indicating no meteors found
    """
    
    recclass_list = [recclass.lower() for recclass in recclass.split('"')]
    recclass_string = "".join(recclass_list)

    result = []
    for i in meteors:
        if i[METEOR_RECCLASS].lower()  == recclass_string:
            result.append(f"The Meteor {i[METEOR_NAME]} ID: {i[METEOR_ID]}")  
    if result:
        return '\n'.join(result)
    else:
        return(f"No meteors found with that recclass")

        

# Chris primarily implemented the geopoint function
def geo_point(meteors,lat,lon):
    """Searches through list of meteors and returns sightings for the designated global coordinates.

    Args:
        meteors (list): Ordered list of meteor sightings
        geopoint (float): Two floating point numbers separated by a comma

    Returns:
        str: A formatted string of result or message indicating no meteors were found.
    """

    nearest_meteor = None
    nearest_distance = math.inf
    
    if float(lat) < -MAX_LAT or float(lat) > MAX_LAT or float(lon) < -MAX_LON or float(lon) > MAX_LON:
        raise ValueError("Latitude and longitude is out of range.")

    for i in meteors:
        if i[METEOR_LAT] != "" and i[METEOR_LON] != "":
            latitude = float(i[METEOR_LAT])
            longitude = float(i[METEOR_LON])
            great_circle = haversine(float(lat),float(lon),latitude, longitude)
            
        if great_circle < nearest_distance:
            nearest_distance = great_circle
            nearest = i
            
    if nearest:
        return (f"The Meteor {nearest[METEOR_NAME]} with ID: {nearest[METEOR_ID]} Named Type: {nearest[METEOR_NAMETYPE]} Recclass: {nearest[METEOR_RECCLASS]} Mass (g): {nearest[METEOR_MASS]} and Fall Type: {nearest[METEOR_FALL]} landed closest to that location in: {nearest[METEOR_YEAR]}")
      
# Vincent implemented entire haversine function  
def haversine(lon1, lat1, lon2, lat2):
    """Calculate the great circle distance in kilometers between two points. (Specified in decimal degrees)
    
    Taken from: Michael Dunn
    https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points

    Args:
        lon1 (_float_): Input Longitude
        lat1 (_float_): Input Latitude
        lon2 (_float_): Listed Longitude
        lat2 (_float_): Listed Latitude
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of Earth in kilometers
    return c*r

# Chris implemented the high_mass function
def high_mass(meteors, num_of_meteors):
    """ Generate a list of the highest mass meteors according to the meteorite_landings_full.csv

    Args:
        meteors (_list_): Ordered list of meteor sightings
    """
    num_of_meteors = int(num_of_meteors)
    try:
        sorted_meteors = sorted(meteors, key=lambda x: float(x[METEOR_MASS] or 0), reverse=True)
    except ValueError:
        raise ValueError("Error converting mass to float. Mass values are invalid.")
    
    if num_of_meteors <= 0:
        raise ValueError("The number of meteorites must be greater than 0")
    
    result = []
    for meteor in range(min(num_of_meteors, len(sorted_meteors))):
        i = sorted_meteors[meteor]
        result.append(f"The meteor {i[METEOR_NAME]} ID: {i[METEOR_ID]} Mass (g): {i[METEOR_MASS]} Recclass: {i[METEOR_RECCLASS]}")
        
    if result:
        return '\n'.join(result)
    return f"No meteors found"

# Chris implemented the count_class function
def count_class(meteors):
    """ Generate a count of the meteors in each unique class under the "fall" category.

    Args:
        meteors (_list_): Ordered list of meteor sightings
    """
    fall_count = {}
    
    for meteor in meteors:
        fall_type = meteor[METEOR_FALL]
        if fall_type:
            if fall_type in fall_count:
                fall_count[fall_type] += 1
            else:
                fall_count[fall_type] = 1
    if fall_count:
        return '\n'.join([f"{fall}: {count}" for fall, count in fall_count.items()])
    return "No meteors found at all"

if __name__ == "__main__":
    main()