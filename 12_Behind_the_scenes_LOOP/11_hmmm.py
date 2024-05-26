import time
username = "Azlan Ali Baig"
email = "azlanbaigbaig@gmail.com"
# print(username)
# print(email)

# f = open('11_hmmm.py')
# print(iter(f) is f)

my_list = [1,2,3,4]
print(iter(my_list) is my_list)

D = {'name':"Azlan",'ID':'18379'}

for key in D.values():
    print(key)