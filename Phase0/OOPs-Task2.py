"""
1.  Why did we put display() inside the class instead of making it a normal function?
Ans the OOP principle of bundling data and behavior together.
    This idea is called Encapsulation.
    
2.  What is the difference between:
    student1.name and student1.display()
Ans student1.name is an attribute (instance variable)
    It stores data.
    student1.display() is a method
    It performs an action.

"""

class Student:
    def __init__(self, student_id, name, course):
        self.id = student_id
        self.name = name
        self.course = course

    def display(self): #self refers to the current object.
        print("Student_Id:",self.id)
        print("Student_Name:",self.name)
        print("Student_Course:",self.course)

student1 = Student("101", "Sidd", "Btech")
student2 = Student("102", "Ibraheem", "Btech")

student1.display() # work internally { Student.display(student1) }
student2.display() # work internally { Student.display(student2) }