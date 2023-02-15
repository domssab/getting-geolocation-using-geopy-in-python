# install geopy library using the 'pip install geopy' in terminal
# import the geopy library
from geopy.geocoders import Nominatim

def start():
# make user choose between location or coordinates
    print("Here are your options:"
        "\n1. Location"
        "\n2. Coordinates",
        "\n3. Exit")
    while True:
        options = input("Location or Coordinates?: ")

# if the user chose option 1
        if options == '1':
    # call the Nominatim tool
            loc = Nominatim(user_agent="GetLoc")

    # asking user to input location
            location = input("Location: ")
            getLoc = loc.geocode(location)

    # printing address
            print(getLoc.address)

    # printing latitude and longitude
            print("Latitude = ", getLoc.latitude, "\n")
            print("Longitude = ", getLoc.longitude)

# if the user chose option 2
        if options == '2':
    # call the Nominatim Tool
            geoLoc = Nominatim(user_agent="GetLoc")

    # asking user to input the coordinates
            coordinate = input("Coordinates: ")
            locname = geoLoc.reverse(coordinate)

    # printing the address/location name
            print(locname.address)

# if the user chose option 3
        if options == '3':
            print("Thank you!")
            break

        else:
            print("Make sure you input the right number.")
start()