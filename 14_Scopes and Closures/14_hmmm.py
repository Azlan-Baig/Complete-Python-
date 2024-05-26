# username = "Azlan Ali Baig"

# def fnc():
#     # username = "Shahzaib"
#     print(username)
# print(username)    
# fnc()

x = 99
# def add(y):
#     z = x + y
#     return z
# result = add(1)
# print(result)


# bad practice hai ye nahi karna, yaani ki global variable ki value change nahi karni ok... :)
# def fnc2():
#     global x  
#     x = 13
    
# fnc2()    
# print(x)

# def f1():
#     x = 14
#     def f2():
#         print(x)
#     return f2   
# result = f1()   
# result()

def code(num):
    def actual(x):
        return x ** num
    return actual   
result = code(2)
print(result(3))
