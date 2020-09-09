# In an if condition we check the conditional
# operators
# marks = 70
# if (marks > 70):
#     print("You got an A")
# elif (marks > 80):
#     print("You got an B")
# elif (marks > 70):
#     print("You got an C")
# else:
#     print("none of the above statemeent gave true")
#     print("you got an F")
# print("outside the if/else")

# marks = 53
# if (marks >= 50 and marks % 2 == 0):
#     print("the no is greater than 50 & even")
# else:
#     if marks == 51:
#         print("the no is 51")
#     print("the no is odd")

# elif is not necessary but if it is used it
# should be used after an if

# else is also not necessary
# else should also be used only after an if or 
# elif


# In human words
# if if fails then if there is an elif 
# condition
# then that is checked


# a = 100
# b = 50
# if a == 100 and b == 50:
#     print(1)
#     if a == 100:
#         print(2)
#     if b == 50:
#         print(3)
#     elif a == 100:
#         print(4)
#     else:
#         print(10)
#     print(5)
# else:
#     print(6)
# print(7)

# a = 5
# b = 10
# if a + b > 15:
#     print(1)
# elif a + b == 15:
#     print(2)
#     if a == 5:
#         print(3)
#     else:
#         print(4)
#     if b == 10:
#         print(5)
#     else:
#         print(6)
#     if a == 5 and b == 10:
#         print(7)
#     if a == 5 or b == 8:
#         print(8)
# else:
#     print(9)
# print(10)
# name = "rahul"
# age = 10

# if True:
#     if age == 10:
#         print(1)
#     else:
#         print(2)
    
#     if age * 4 > 20:
#         print(3)
#         print(4)
#     elif age * 2 >= 20:
#         print(5)
#         print(6)
#     else:
#         print(7)
# print(8)
# if age == 10:
#     print(9)
#     print(10)
# print(11)


# if False:
#     print(0)
# else:
#     if True or False:
#         print(1)
#     elif True and True:
#         print(2)
#     if False and False:
#         print(3)
#     print(4)



if 1 == 1:
    print(0)
    if 2 == 1 + 1:
        print(1)
        a = 5
        if a % 2 == 0:
            print(2)
        else:
            print(3)
        print(4)
    print(5)
print(6)