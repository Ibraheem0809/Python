students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice:")
    if choice == "1":
        id = input("Enter Student ID:")
        name = input("Enter Student Name:")
        course = input("Enter Course Name:")

        student = {
            "id" : id,
            "name" : name,
            "course" : course
        }

        students.append(student)
        print("Student ADDED Successfully!")
    elif choice == "2":
        if len(students) == 0:
            print("Student NOT Found!")
        else:
            i = len(students)
            print("\nStudent Records:")
            for student in students:
                print(student)
            print("Total number of Students: ",i)
    elif choice == "3":
        delete_id = input("Enter Student ID to Delete: ")
        found = False
        for student in students:
            if student["id"] == delete_id:
                students.remove(student)
                found = True
                print("Student DELETED Successfully!")
                break
        if not found:
            print("Student NOT Found")
    elif choice == "4":
        search = input("Enter Student Name:")
        found = False
        for student in students:
            if student["name"].lower() == search.lower():
                print("\nStudent Found")
                print(student)
                found = True
        if not found:
            print("Student NOT Found")
    elif choice == "5":
        name = input("Enter Student Name to be Updated: ")
        found = False
        for student in students:
            if student["name"].lower() == name.lower():
                up_id = input("Enter Updated Id")
                up_name = input("Enter Updated Name")
                up_course = input("Enter Updated Course")
                student["id"] = up_id
                student["name"] = up_name
                student["course"] = up_course
                found = True
                print("Student Updated Successfully!")
                break
        if not found:
            print("Student NOT Exist.\nTRY AGAIN!")

    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid Choice")