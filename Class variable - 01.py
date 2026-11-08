
# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    class_year = 2026

    def __init__(self,name,age):
        self.name = name
        self.age = age

student1 = Student("Kye",28)
student2 = Student("Kelly",50)

print(student1.name)
print(student1.age)
print(Student.class_year)