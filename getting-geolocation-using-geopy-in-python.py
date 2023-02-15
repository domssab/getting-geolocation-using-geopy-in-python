# install geopy library using the 'pip install geopy' in terminal
# import the geopy library
from geopy.geocoders import Nominatim

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# make user choose between location or coordinates
print("Here are your options:"
      "\n1. Location"
      "\n2. Coordinates",
      "\n3. Exit")

# entering the location name
location = input("Location: ")
getLoc = loc.geocode(location)

# printing address
print(getLoc.address)

# printing latitude and longitude
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)