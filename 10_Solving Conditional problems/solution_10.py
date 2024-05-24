pet = input("Enter type of pet: ")
age = int(input("Enter you pet age: "))

if pet == "Dog":
    if age<2:
        print("Puppy Food")
    else:
        print("Adult Dog Food")
elif pet == "Cat":
    if age>5:
        print("Senior cat food")
    else:
        print("Junior cat food")
        
            