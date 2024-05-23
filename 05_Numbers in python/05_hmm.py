#  YE SAARAY K SAARAY PRINT STATEMENTS K SAATH YAHEIN YA PHIR PYTHON SHELL PAR CHECK KAR SAKTAY HAUN.



x = 2 
y = 3 
z = 4 
x + y 
40 + 2.23 

# 'Azlan' + 2 

int(2.23) 
float(40)
'chai' + 'code'
 
z ** 5 

# print(2**1000)


# ASSIGNMENT: Find Differnces between repr, str and print:) 

x < y and y < z 

1 == 2 < 3 
1 == 2 and 2 < 3

import math
math.floor(3.5)
math.floor(-3.5)
math.floor(3.6)
math.floor(3.9)   # Math.floor() aapko hamesha bottom values k paas leke jaata hai,
math.trunc(2.7)
math.trunc(-2.7)  # truncte aapko hamesha  0 ki taraf lekar jaata hai .

# COMPLEX NUMBERS IN PYTHON
2 + 3
(2+3j) * 3

0o20 # Octal numbers
0xFF # Hex numbers 
0b1000  # binary numbers 


#Conversion
oct(64)
hex(64)
bin(64)

# esay bh hu sakta hai.

int('64', 8)
int('64', 16)
int('10000', 2)

import random
random.random()
random.randint(1,10)
l1 = ['chai','cofe', 'agram bagram']
random.choice(l1)
random.shuffle(l1)

# print((0.1+0.1+0.1) - 0.3 )

from decimal import Decimal

x = Decimal('0.3') + Decimal('0.3') + Decimal('0.3')  -  Decimal('0.3')
print(x)


from fractions import Fraction

Fraction(2,7)

setOne = {1,2,3,4}
a = setOne & {1,4} # Intersection
print(a)

b = setOne | {1,5} # Union
print(b)

c = setOne - {1,2,3,4}
print(c)