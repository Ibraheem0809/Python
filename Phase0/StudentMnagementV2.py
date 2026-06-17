import json

FILE_NAME = "students.json"

"""
    Saving:                             Loading:
    
        Python List                         students.json
         ↓                                         ↓
        json.dump()                         json.load()
         ↓                                         ↓
        students.json                       Python List

"""

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    student_id = input("Enter Student ID: ").strip()

    # Check duplicate ID
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course Name: ").strip()

    if not student_id or not name or not course:
        print("All fields are required!")
        return

    student = {
        "id": student_id,
        "name": name,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student Added Successfully!")


def view_students(students):
    if not students:
        print("No students available.")
        return

    print("\n===== STUDENT RECORDS =====")

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Course: {student['course']}"
        )

    print(f"\nTotal Students: {len(students)}")


def delete_student(students):
    student_id = input("Enter Student ID to Delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)

            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


def search_student(students):
    student_id = input("Enter Student ID to Search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\n===== STUDENT FOUND =====")
            print(f"ID     : {student['id']}")
            print(f"Name   : {student['name']}")
            print(f"Course : {student['course']}")
            return

    print("Student Not Found!")


def update_student(students):
    student_id = input("Enter Student ID to Update: ").strip()

    for student in students:
        if student["id"] == student_id:

            print("\nCurrent Details")
            print(f"ID     : {student['id']}")
            print(f"Name   : {student['name']}")
            print(f"Course : {student['course']}")

            new_name = input("Enter New Name: ").strip()
            new_course = input("Enter New Course: ").strip()

            if new_name:
                student["name"] = new_name

            if new_course:
                student["course"] = new_course

            save_students(students)

            print("Student Updated Successfully!")
            return

    print("Student Not Found!")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            delete_student(students)

        elif choice == "4":
            search_student(students)

        elif choice == "5":
            update_student(students)

        elif choice == "6":
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()