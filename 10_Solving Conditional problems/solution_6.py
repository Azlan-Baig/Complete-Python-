distance = int(input("Enter Distance in KM: "))
if distance <3:
    way_of_transport = "walk"
if distance <15:
    way_of_transport = "Bike"
if distance >15:
    way_of_transport = "Car"

print(way_of_transport)