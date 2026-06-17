"""
super() - Call the constructor of the parent class.

"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Student_name:",self.name)
        print("Student_age:",self.age)

class Student(Person):
    def __init__(self,name,age,course):
        super().__init__(name, age)
        self.course = course

    def display2(self):
        print("Student_name:",self.name)
        print("Student_age:",self.age)
        print("Student_course:",self.course)

student1 = Student("Sidd","20","Btech")

student1.display()
student1.display2()
