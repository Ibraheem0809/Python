"""
1. What is Student?
Ans - Student is a class that defines the blueprint of every student 

      A class is a blueprint/template that defines:
      Properties (data)
      Behaviors (methods)

2. What is student1?
Ans - student1 is an object that is created on the basis of Student
      Student → Class = (Blueprint)
      student1 → Object (Instance) = (Actual Things)

3. What is the purpose of __init__()?
Ans - __init__() is a constructor.
      It runs automatically whenever an object is created.

4. What does self represent?
Ans - self refers to the current object.

"""

class Student:
    
    def __init__(self, student_id, name, course):
        self.id = student_id
        self.name = name
        self.course = course

student1 = Student("101","Sidd","B-Tech")

print(student1)
print(student1.id)
print(student1.name)
print(student1.course)

