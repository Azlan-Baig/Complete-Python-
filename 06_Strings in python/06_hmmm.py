# chai = "Masala Chai"
# slice_chai = chai[0:6]
# print(slice_chai)
# numlist = "0123456789"
# print(numlist[:])
# print(numlist[3:])
# print(numlist[:7])
# print(numlist[0:7:2])
# print(numlist[0:8:3])
# print(chai.lower())
# print(chai.upper())

# chai = "     Masaala chai     "
# print(chai.strip()) #Removes extra spaces from the string.
# print(chai.replace("Masala", "Ginger"))  # Original string change nahi karega..
# print(chai)




# CONVERTING STRING TO LISTS.

# chai = "Lemon, Ginger, Masala, Mint"
# print(chai.split())
# print(chai.split(", "))

# print()


# chai = "Masala Chai"
# print(chai.find("Chai")) 
# print(chai.find("chai"))   # -1 matlab mjhay value nahi miley to menay -1 return kardia 
# quantity = 2

# order = "I ordered {} cups of {}."

# # print(order.format(quantity,chai))

# # CONVERTING LISTS TO STRING.
# chai_variety = ["Lemon", "Ginger", "Masala"]
# print(", ".join(chai_variety))

chai = "He said , \"Masala Chai is awesome\""
# print(chai)

chai = "masala\nchai"
# print(chai)
# ab agar me chahta hun k mme y apay string me \n string use karna chahta hun to esay raw string likhney paregey.
chai = r"masala\nchai"
# print(chai)
chai = r"c:\user\pwd"
print(chai)