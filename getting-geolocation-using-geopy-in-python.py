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
        options = input("Location or Coordinates?: ")

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
            getLoc1 = loc.geocode(location1)

            location2 = input("Input the second location: ")
            getLoc2 = loc.geocode(location2)

            print("Coordinates of", location1, "is: ", getLoc1.latitude,",",getLoc2.longitude)

            coordinate1 = input("Enter the first coordinates (La/Lo): ")
            coordinate2 = input("Enter the first coordinates (La/Lo): ")

            print("The distance between", coordinate1, "and", coordinate2, "is: ",GD(coordinate1,coordinate2).km)

# if the user chose option 4
        elif options == '4':
            print("Thank you and have a nice day!")
            break

        else:
            print("Please make sure you input the right number.")

start()