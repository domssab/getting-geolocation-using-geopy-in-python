# install geopy library using the 'pip install geopy' in terminal
# import the geopy library
from geopy.geocoders import Nominatim

# make user choose between location or coordinates
print("Here are your options:"
      "\n1. Location"
      "\n2. Coordinates",
      "\n3. Exit")
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

if options == '2':
# importing modules
from geopy.geocoders import Nominatim

# calling the nominatim tool
geoLoc = Nominatim(user_agent="GetLoc")

# passing the coordinates
locname = geoLoc.reverse("26.7674446, 81.109758")

# printing the address/location name
print(locname.address)