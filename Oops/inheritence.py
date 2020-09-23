# class Animal:
#     def __init__(self, name, age, no_of_legs):
#         self.name = name
#         self.age = age

#     def sleep(self):
#         print("Animal ", self.name, "sleeps")

#     def walk(self):
#         print("Animal", self.name, "walks")

#     def sleepAndWalk(self):
#         self.sleep()
#         self.walk()
    

# class Dog(Animal):
#     def __init__(self, name, age, no_of_legs, no_of_teeths):
#         super().__init__(name, age, no_of_legs)
#         self.teeth = 'canine'
#         self.tail = True
#         self.no_of_teeths = no_of_teeths
    
#     def bark(self):
#         print("Dog barks ", self.name)


# class Cat(Animal):
#     def __init__(self, name, age, no_of_legs):
#         super().__init__(name, age, no_of_legs)


# if __name__ == '__main__':
#     # animal = Animal("dog", 15, 4)
#     # animal.walk()

#     dog = Dog("bruno", 14, 4, 32)
#     print(dog.teeth)
#     print(dog.name)
#     print(dog.teeth)
#     dog.walk()
#     dog.bark()

#     # cat = Animal("cat", 10, 4)
#     # # cat.sleep()
#     # # cat.walk()

#     # cat.sleepAndWalk()


# class Father:
#     def __init__(self):
#         self.surname = "narang"

#     def can_sing(self):
#             print("singing")

# class Son(Father):
#     def can_dance(self):
#         print("dancing")



# if __name__ == '__main__':
#     son1 = Son()
#     son1.surname = "abcd"
#     print(son1.surname)
#     son2 = Son()
#     print(son2.surname)


# class Parent:
#     def __init__(self):
#         self.name = "abc"

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.name = "bcd"

# c = Child()
# print(c.name)


# Abstraction: Hiding the implementation is known as abstraction
# CheckAuthenticatedPassword.checkPassword(password):
    #  

# Polymorphishm -> same thing can do different stuff or behave differently based on arguments passed

# "str" + "bcd" = concatenate ("strbcd")
# 1 + 5 =   6
# [1,2 ] + [5,6] = [1,2,5,6]

# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class Rectangle(Shape):
#     def __init__(self, x, y):
#         super().__init__(x, y)

#     def compute_area(self):
#         return self.x * self.y

# class Triangle(Shape):
#     def __init__(self, base, height):
#         super().__init__(base, height)
    
#     def compute_area(self):
#         return ((1 / 2) * self.x * self.y)


# if __name__ == '__main__':
#     rectangle = Rectangle(100, 10)
#     print(rectangle.compute_area())

#     triangle = Triangle(100, 10)
#     print(triangle.compute_area())

