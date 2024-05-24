chai_types = {
    "Masala" : "Spicy",
    "Ginger": "Zesty",
    "Green" : "Mild"
}

# print(chai_types[ "Masala"])
# print(chai_types.get("Ginger"))
chai_types["Masala"]  = "Not Spicy"
# print(chai_types)


# for chai in chai_types:
#     print(chai_types)

# for chai in chai_types:
#     print(chai,chai_types[chai])   
    
    
# for key, value in chai_types.items():
#     print(key,value)    

# if "Green" in chai_types:
#     print("Masala chai hai")    


chai_types["Earl grey "] = "Citrus"
# print(chai_types)

chai_types.pop("Masala")
# print(chai_types)
# print(chai_types.popitem())

tea_shop = {
    "chai" : {
        "Masala": "Spicy",
        "Ginger" : "Zesty"
    },
    "tea": {
        "Green" : "Mild",
        "Black" : "Strong"
    }
}

# print(tea_shop["chai"]["Masala"])

squared_num = {
    x:x**2 for x in range(1,10)
}

print(squared_num)

# squared_num.clear()

keys = ["Toyota", "Suzuki", "Honda"]
default_values = "1200cc"

new_dict = dict.fromkeys(keys,default_values)
print(new_dict)