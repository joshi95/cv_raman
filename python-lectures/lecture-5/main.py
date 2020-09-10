# while loop syntax
# i = 5
# while (i > 0):
#     print("hello", i)
#     i -= 1

# # for loop syntax
# print("first")
# i = 0
# for j in range(0, 5, 1):
#     print("hello", j)
#     i += 1
#     print("the value of j is ", i)
# print("last")

# print all the even no in range 1-50
# write a program which will print 
# no divisible by 4 and 3 in range(1, 50)

# 4 is divisible by 4
# 6 is divisible by 3
# 8 is divisible by 4
# 9 is divisible by 3
# 12 -> is divisible by 4 and 3 both
# n = int(input())
# for i in range(1, n):
#     if i % 3 == 0 and i % 4 ==0:
#         print(i, "divisible by both")
#     elif i % 4 == 0:
#         print(i, "divisible by 4")
#     elif i % 3 == 0:
#         print(i, "divisible by 3")

# print("start")
# for i in range(0, 10):
#     print("iteration ", i)
#     if i >= 5:
#         continue
#     print("working for ", i)
# print("end")


# we will be making a calculator

# Hey this is the awesome calculator
# These are the operations supported by it
# 1. Addition
# 2. Mulitplication
# 3. Divisision
# 4. Subtraction
# 5. Sqrt
# Press x to exit
# Please enter value for x
# Please enter value for y
# Please give the operation you want to do.
# if the operation is 1 you will do addtion/sub

# print(
#         """
#         Hey this is the awesome calculator
#         These are the operations supported by it
#         # 1. Addition
#         # 2. Mulitplication
#         # 3. Divisision
#         # 4. Subtraction
#         # 5. power (x, y)
#         # 6. exit
#         """
#     )

# while True:
#     print("please enter the value of x: ")
#     x = float(input())
#     print("please enter the value of y: ")
#     y = float(input())
#     print("Please enter the operation code: ")
#     operation = int(input())

#     if operation == 6:
#         print("Please come back again tomorrow !! :) ")
#         break
#     res = 0
#     if operation == 1:
#         res = x + y
#     elif operation == 2:
#         res = x * y
#     elif operation == 3:
#         res = x / y
#     elif operation == 4:
#         res = x - y
#     elif operation == 5:
#         res = x ** y
#     else:
#         print("invalid opration")
#         continue
#     print("the result of the operation is ", res)


for i in "ABCDEFGH":
    print(i, "is the character")