tea_varieties = ["Black","Green","Oolong","White"]
# print(tea_varieties[0])
# print(tea_varieties[-1])
# print(tea_varieties[1:3])
tea_varieties[3] = "Herbal"

# print(tea_varieties)

# tea_varieties[1:2] = "Lemon" # Dont replace the value like this, check the output of this and you will find out.
# print(tea_varieties)

# tea_varieties[1:2] = ["Lemon"] # Will work fine now
# print(tea_varieties)

tea_varieties[1:1] = ['test','test']
# print(tea_varieties)
# print(tea_varieties[1:3])
tea_varieties[1:3] = [] # matlab k in positions par kuch nahi huna chahiye, delete operations bh keh saktay isay.
# print(tea_varieties)

# for tea in tea_varieties:
    # print(tea)
    # print(tea, end="-")
    
if "Masala" in tea_varieties:
    print("I have Masala tea")
else:
    tea_varieties.append("Masala")
    
# print(tea_varieties)        
tea_varieties.pop()
# print(tea_varieties)
tea_varieties.remove("Black")
# print(tea_varieties)
tea_varieties.insert(1, "Doodh Patti")
# print(tea_varieties)
tea_varieties_copy = tea_varieties.copy()  # Memory me reference alag karnay k liye ye copy() method use hota hai.
        
# THIS IS CALLED LIST COMPREHENSION

myL = [x**2 for x in range(1,10)]    
print(myL)