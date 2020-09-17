# # # fruits = list()

# # # fruits.append("ABC")
# # # fruits.extend(["ABC", "BCD"])

# # # print(fruits)
# # # print(len(fruits))

# # # pop(idx) -> remove the idx item in the list
# # # pop() -> remove the last value from the list

# # # fruits = ["apple", "banana", "choclate", "abc"]

# # # for i in range(0, len(fruits)):
# # #     print(fruits[i])

# # # List comprehension

# # # A = [j for j in range(1, 10, 2)]

# # # print(A)
# # list() or []
# # # List -> mutable (you can change it once assigned)
# # # Tuples -> immutable (you cannot change them once you have assigned)

# # fruits_tuple = ("apple", "banana", 1, 2, 5)
# # print(len(fruits_tuple))
# # slice_tuple = fruits_tuple[1:]
# # print(type(slice_tuple))
# # print(slice_tuple)

# # Dictionary
# dict() or {}
# # key: values mutable also
# top_marks = {"A": 120, "B": 200, "C": 40}
# # dictionary -> you can use idexing by key
# print(top_marks["A"])
# print(top_marks["C"])
# print(len(top_marks))
# print("earlier", top_marks)
# top_marks["D"] = 500
# top_marks[7] = 1000
# print("after", top_marks)
# print(top_marks[7])

# # delete a key from a dictionary
# top_marks.pop(7)
# print(top_marks)

# # to get all the keys present in dictinary
# print(list(top_marks.keys()))
# values_of_dict = list(top_marks.values())
# print(values_of_dict)


# # items -> [(key1, value1), (key2, value2), ()]
# print(top_marks)
# print("items", top_marks.items())


# student_roll_no_to_name = {1: "Sadaf", 2: "Abhijeet", 3: "Abhinav"}
# print(student_roll_no_to_name)

# [('key1', 'value1'), ('key2', 'value2'),]
# for entry in student_roll_no_to_name.items():
#     print("key", entry[0], "value", entry[1])
    
# for key in student_roll_no_to_name.keys():
#     print("key", key, "value", student_roll_no_to_name[key])

# for key, value in student_roll_no_to_name.items():
#     print("key", key, "value", value)

