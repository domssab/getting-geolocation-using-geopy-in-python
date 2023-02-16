# install geopy library using the 'pip install geopy' in terminal
# import the geopy library
from geopy.geocoders import Nominatim
from geopy.distance import geodesic as GD

def start():
# make user choose between location or coordinates
    print(" ---------------WELCOME---------------"
        "\n|       Here are your options:        |"
        "\n|       1. Location                   |"
        "\n|       2. Coordinates                |",
        "\n|       3. Know the distance          |"
        "\n|       4. Exit                       |"
        "\n -------------------------------------"
        "\n")
    while True:
        options = input("Enter your option: ")

# if the user chose option 1
        if options == '1':
    # call the Nominatim tool
            loc = Nominatim(user_agent="GetLoc")

    # asking user to input location
            location = input("Location: ")
            getLoc = loc.geocode(location)

    # printing address
            print("Address:", getLoc.address)

    # printing latitude and longitude
            print("Latitude = ", getLoc.latitude,)
            print("Longitude = ", getLoc.longitude)

            try_again = input("Would you like to try again?(yes/no): ")
            if try_again == "yes":
                continue
            else:
                print("Thank you!")
                break

# if the user chose option 2
        elif options == '2':
    # call the Nominatim Tool
            geoLoc = Nominatim(user_agent="GetLoc")

    # asking user to input the coordinates
            coordinate = input("Coordinates (Latitude, Longitude): ")
            locname = geoLoc.reverse(coordinate)

    # printing the address/location name
            print(locname.address)


            try_again = input("Would you like to try again?(yes/no): ")
            if try_again == "yes":
                continue
            else:
                print("Thank you!")
                break

# if the user chose option 3
        elif options == '3':
            locate = Nominatim(user_agent = "GetLoc")

            location1 = input("Input the first location: ")
            getLoc1 = locate.geocode(location1)

            location2 = input("Input the second location: ")
            getLoc2 = locate.geocode(location2)

            coordinates1 = getLoc1.latitude, getLoc1.longitude
            coordinates2 = getLoc2.latitude, getLoc2.longitude

            print("Coordinates of", location1, "is: ", coordinates1)
            print("Coordinates of", location2, "is: ", coordinates2)

            print("The distance between", location1, "and", location2, "is: ",GD(coordinates1,coordinates2).km)


            try_again = input("Would you like to try again?(yes/no): ")
            if try_again == "yes":
                continue
            else:
                print("Thank you!")
                break
# if the user chose option 4
        elif options == '4':
            print("Thank you and have a nice day!")
            break

        else:
            print("Please make sure you input the right number.")

start()