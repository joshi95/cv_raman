# # # # # # array

# # # # # # # declaration
# # # # # # fruits = ["apple", "banana", "pineapple"]

# # # # # # # or 
# # # # # fruits = list()
# # # # # print(fruits)
# # # # # fruits.append("apple")
# # # # # print(fruits)
# # # # # fruits.append("banana")
# # # # # print(fruits)
# # # # # fruits.append("pineapple")
# # # # # print(fruits)

# # # # # # # # or
# # # # # # fruits = list()
# # # # # # apple = ["red apple", "green apple"] 
# # # # # # banana = ["red banana", "yellow_banana"]
# # # # # # pineable = ["pineapple"]

# # # # # # fruits.extend(apple)
# # # # # # fruits.extend(banana)
# # # # # # fruits.extend(pineable)

# # # # # # print(fruits)

# # # # ############ 

# # # # # + -> 5 + 7 = 12
# # # # # + -> "ram" + "rohan" = ratrohan
# # # # # + -> to data types are of list then it will behave like extend

# # # # # summer_fruits = ["apple", "banana"]
# # # # # winter_fruits = ["grapes", "mango"]

# # # # # fruits = summer_fruits + winter_fruits

# # # # # print("summer fruits ", summer_fruits)

# # # # # print("winter fruits ", winter_fruits)

# # # # # print("all fruits ", fruits)


# # # # # a = [1,2,3,4]
# # # # # b = ["a", "b", "c", "d"]
# # # # # c = a + b
# # # # # a = "a"
# # # # # b = "b"
# # # # # c = "c"
# # # # # d = "d"
# # # # # b = [a, b, c, d]


# # # # a = ["abc", "def"]
# # # # b = [3, 4, str(5) + "s"]
# # # # c = a.extend(b)
# # # # print(c)
# # # # print(a)


# # # # Program to add an s to each array element

# # # items = ["pen", "pencil", "book", "rubber"]
# # # quantity = [10, 5, 6, 3]

# # # # ith item quantity is the ith quantity
# # # # Output : I have 10 pens, 5 pencils, 6 books and 3 rubber

# # # # hint : you all know how indexing works ! and for loop.

# # #   0        1        2        3
# # # ["pen", "pencil", "book", "rubber"]
# # # [10,       5,       6,        3]


# # # I have 10 pens, 5 pencils, 6 books and 3 rubber
# # items = ["pen", "pencil", "book", "rubber", "stapler"]
# # quantity = [1, 5, 1, 2, 6]

# # # I have 1 pen, 5 pencils, 1 book and 2 rubbers

# # print("I have ", end="")
# # for i in range(0, 5):
# #     if quantity[i] > 1:
# #         item_string = items[i] + "s"
# #     else:
# #         item_string = items[i]

# #     if i == 3:
# #         print(quantity[i], item_string, end=" and ")
# #     elif i < 3:
# #         print(quantity[i], item_string, end=", ")
# #     else:
# #         print(quantity[i], item_string)



# # # List Methods
# # 1. append
# # 2. extend
# # 3. indexing
# # 4. slicing

# # A[:] -> copies the array
# # A[:idx] -> will give an array from starting till idx - 1
# # A[idx: ] -> will give an array from idx to end
# # A[::-1] -> will give reverse the array


# A = [1, 2, 3, 4, "apple", "banana"]

# print(A[:4], A[::-1])

