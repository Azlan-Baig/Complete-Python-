
# RUN THESE IN TERMINALS

 f = open('11_hmmm.py')\
 f.readline()

#    Isey file ko ab esay read kar k dekho
f.__next__() #Stop iteration ka error ayega. wohey jo theory parhyy thyy..

for line in open('11_hmmm.py'):
     print(line,end="")

f = open('11_hmmm.py')
while True:
     line = f.readline()
     if not line: break
     print(line,end='')     

myList = [1,2,3,4]
I = iter(myList)     
I
I.__next__()
I
I.__next__()
I.__next__()
I.__next__()
