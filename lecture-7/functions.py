# def greet():
#     print("Good Morning")
#     print("Hello!")

# def wish():
#     print("Happy Birthday")
    
# def is_possible():
#     return True

# def printName():
#     return "Keval"

# def printInt():
#     return 56

# def printFloat():
#     return 45.0


# def isNoGreaterThanSeven(no):
#     if no > 7:
#         return True
#     else:
#         return False

# def alwaysTrue(no, sec, third, fourth):
#     print("This function will return True if the no is even")
#     print("Else it will return False")
#     if no % 2 == 0:
#         return True
#     else:
#         return False

# def printRandom(firstVar, secVar, thirVar):
#     print(firstVar, secVar, thirVar)
#     return True

# def test(a):
#     print("will check equal condition for 5")
#     if a == 5:
#         return 5
#     print("will check equal condition for 7")
#     if a > 3:
#         return 7
#     print("nothing got executed will return the no")
#     return a


# out = test(5)
# print(out)




# # # ###############
# # # print("Good Morning")
# # # print("Hello!")

# # # print("Happy Birthday")

# # # print("Good Morning")
# # # print("Hello!")

# # # print("Good Morning")
# # # print("Hello!")

# # # print("Good Morning")
# # # print("Hello!")


# # ###

# # def NameOfFunction():
# #     print("abc")
# #     print("bcd")

# # NameOfFunction()


# Question 1:

# def fun(no):
#     if no % 2 == 0:
#         return "yes"
#     return "no"

# print(fun(51))

# Question 2:
# def fun(name):
#     if 'x' in name:
#         return True
#     return False

# print(fun("happy"))

def checkIfEven(no):
    if no % 2 == 0:
        return "even"
    return "odd"


print("checking even ")
no = checkIfEven(50)



def printReverseName(name):
    for i in range(len(name) - 1, 2, -1):
        print(name[i], end="")
    print()

def printChar(name):
    [0,1,2,3,4,5]
    for i in range(0, len(name)):
        print(name[i], end="")
    print()

printReverseName("NamaN")