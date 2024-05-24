char = input("Enter a Password: ")

if len(char)<6 :
    check = "Weak"
elif len(char)<10:
    check = "Medium"
elif len(char)>10:
    check = "Strong"
    
print("Your password is: ", check)            


a = [1,2,3]
