l1 = [1,2,3]
l2 = l1
l1[0] = 55

# print(l1)
# print(l2)
# l2 bh change hua hai jab l1 ko new value de hai q k refernce paas kia hua hai..

l3 = [10,20,30]
l4 = l3
l4 = [10,20,30]

l3[0] = 90 
# print(l3)
# print(l4)

# last time jesa hua thaa wesa nahi huga q k is dafa l4 ko ek khudse list dede hai jo dikhnay me to same hai par uska refernce alag se create hugaya hai memory mein.

l5 = [5,6,7]
l6 = l5[:] # industry me esay copy kartay hain, matlab k copy hojaye sirf reference pass na ho.

# l5[0] = 9

# print(l5)
# print(l6)
# same goes here. 

import copy

# copy.deepcopy()   # is say huta kia hai list k andar bh koi list hutey hai to wo bh copy hojaatey hai .

print(l5==l6)
print(l5 is l6 )