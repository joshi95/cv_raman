"""
# # # # Model real world to code
# # # # Their are attributes and methods in real world

# # # # The class name should always begin with a capital letter
# # # class Airplane:
# # #     # dunder method or constructor
# # #     def __init__(self, company_name, no_of_passengers, seats):
# # #         # you make attributes like this in a class
# # #         self.company_name = company_name

# # #         self.no_of_passengers = no_of_passengers
        
# # #         self.seats = seats

# # #     # methods ... each function will have a self as first argument

# # #     def take_off(self, message):
# # #         print(self.company_name, " airoplane takes off !")
# # #         print("the aeroplane said", message)

# # #     def land(self, one, two, three):
# # #         print("landing ", one, two, three)

# # #     def fly(self):
# # #         print("aeroplane flies")


# # # if __name__ == '__main__':
# # #     print("print will be creating an aeroplane here")

# # #     # creating a class object
# # #     kingfisher_airlines = Airplane("kingfisher", 50, 100) # syntax for creating an object
    
# # #     print(kingfisher_airlines.company_name)

# # #     vistara_airlines = Airplane("vistara", 100, 100)
    
# # #     print(vistara_airlines.company_name)


# # #     kingfisher_airlines.take_off("Have a nice flight")
# # #     vistara_airlines.land(1 ,2, 3)



# # class Student:
# #     def __init__(self, name, roll_no):
# #         self.name = name
# #         self.roll_no = roll_no
# #         self.marks = 0

# #     def set_marks(self, mark):
# #         self.marks = mark

# #     def display_student(self):
# #         print(f"Student name : {self.name} Roll no: {self.roll_no} marks: {self.marks}")



# # class test:
# #     def __init__(self):
# #         self.variable = 'Old'
# #         self.Change(self.variable)

# #     def Change(self, var):
# #         var = 'New'


# # class A:
   
# #     def setNewAge(self, age):
# #         self.age = age

# #     def __init__(self):
# #         self.age = 15
# #         self.setNewAge(67)

# # if __name__ == '__main__':
# #     obj=A()
# #     print(obj.age)
# #     obj.age = 25
# #     print(obj.age)

# # #     rohan = Student("rohan", 1)
# # #     ravi = Student("ravi", 2)
# # #     pragya = Student("pragya", 3)

# # #     all_students = [rohan, ravi, pragya]
    
# # #     for student in all_students:
# # #         student.display_student()


# # # def test(name="ham"):
# # #     print(name)

# # # test()


# class Airplane:

#     def __init__(self, name, age):
#         self.__name = name
#         self.__age =  age
#         self.__password = "abcd"
    
#     def get_age(self):
#         return self.__age

#     def __reveal_password(self):
#         return self.__password
    
#     def show_password(self):
#         return self.__reveal_password()


# if __name__ == '__main__':
#     airplane = Airplane("boeing", 10)
#     #print(airplane.__reveal_password())
#     print(airplane.__sname)
#     #print(airplane.__age)
#     #airplane.print_age()
#     #print(airplane.get_age())
    

# # 4 principles of oops

# # 1. Encapsulation -> hiding the variables and setting private/public access on them.

# # 2. Abstraction
# # 3. Inheritence
# # 4. Polymorphism

# class Check:
#     def __init__(self, age):
#             self.__age = age

#     def get_age(self):
#         return self.__age


# x = input()
# c = Check(int(x))
# print(c.get_age())

# Inheritence

# Animal:
#     eyes:
#     nose:
#     teetch:
#     ears:
#     legs

#     eat()
#     sleep()
#     walk()
#     bite()

# Dog(Animal):
#     bark()
#     be_loyal()
#     tickle()

# Cat(Animal):
#     flexibody
#     jump()
#     eat_rat()
#     say_meow()
    

# LabraDore(Dog):
#     country:

# Pug(Dog):
#    country:
"""
