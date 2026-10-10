import json
print("====================================================================================")
while True:

    print("---------------------------------------------------------------------------------")
    print("\n 1. View students")
    print("2. Search student")
    print("3. Add student")
    print("4. Exit")
    print("---------------------------------------------------------------------------------")

    choice = input("Enter choice: ")

    if choice == "1":
        with open("student.json", "r")as file:
            students = json.load(file)

        for student in students:
            print(
                f"Name {student['name']} |"
                f"Age {student['age']} |"
                f"Course {student['course']} |"
            )

        print("-------------------------------------------------------------------")

    elif choice == "2":
        search = input("Enter student name to search: ").lower()

        with open("student.json", "r")as file:
            students = json.load(file)

        found = False

        for student in students:
            if search == student["name"].lower():
                print("Student found")
                print(
                    f"Name {student['name']} |"
                    f"Age {student['age']} |"
                    f"Course {student['course']} |"
                )
                found = True
                break

        if not found:
            print("Student not found!")

        print("----------------------------------------------------------------------")

    elif choice == "3":
        number = int(input("Enter number of students to add: "))

        with open("student.json", "r")as file:
            students = json.load(file)

        for i in range (number):
            name = input("Enter student name: ").lower()
            age = int(input("Enter age of student: "))
            course = input("Enter course of student: ").lower()

            student = {
                "name": name,
                "age": age,
                "course": course
            }
            students.append(student)

        with open("student.json", "w")as file:
            json.dump(students, file, indent=4)

        print("--------------------------------------------------------------------")

    elif choice == "4":
        print("Auf weidersehn!")
        break

    else:
        print("Invalid choice!")
print("====================================================================================")
print("====================================================================================")
