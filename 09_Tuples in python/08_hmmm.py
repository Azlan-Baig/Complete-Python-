# LIST OR TUPLES ME MAIN DIFFERENCE YE HAI K LIST MUTABLE HAI OR TUPLES IMMUTABLE HUTEY HAI.

tea_types = ("Black", "Green", "Oolong")
tea_types[0]
 
# tea_types[0]  = "Yellow" #Error dedega as tuples don't support mutability.


more_tea  = ("Doodh Patti","Cofee")

all_tea = more_tea + tea_types
print(all_tea)
  
(a,b,c)  = tea_types # SAME LIKE DESTRUCTURING.

print(a,b,c)  

print(type(tea_types)) 