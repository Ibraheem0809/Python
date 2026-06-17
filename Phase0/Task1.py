file = open("notes.txt", "w")
file.write("I am learning AI Engineering.")
file.close()


file = open("notes.txt", "a")
file.write("\nI know Python basics.")
file.close()

with open("notes.txt", "a") as file:
    file.write("\nThis is Task - 1")

"""
    Saving:                             Loading:
    
        Python List                         students.json
            ↓                                    ↓
        json.dump()                         json.load()
            ↓                                    ↓
        students.json                       Python List

"""


import json

student = {
    "id" : "101",
    "name" : "Ibraheem",
    "course" : "B-Tech"
}

with open("students2.json", "w") as file:
    json.dump(student,file,indent=4)
print("Student data SAVED Successfully!")

with open("students2.json", "r") as file:
    data  = json.load(file)

print(type(data))
print("Student_id:", data["id"])
print("Student_name:", data["name"])
print("Student_course:", data["course"])
