import csv
print("===============================================================")

while True:
    print("\n 1. View students")
    print("2. Search student")
    print("3. Add students")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        with open("students.csv","r")as file:
            students = csv.reader(file)
            for row in students:
                print(row)

    elif choice == "2":
        search = input("Enter student's name to search: ").lower()

        with open("students.csv", "r")as file:
            students = csv.reader(file)

            found = False 

            for student in students:
                if search == student[0].lower():
                    print("Student found!")
                    print(
                        f"Name {student[0]} |"
                        f"Age {student[1]} |"
                        f"Course {student[2]} |"
                    )
                    found = True
                    break
            if not found:
                print("Student not found!")

    elif choice == "3":
        number = int(input("Enter number of students to add: "))
        for i in range(number):
            name = input("Enter name of student: ").lower()
            age = int(input("Enter age of student: "))
            course = input("Enter course: ").lower()

            students = {
                "name": name,
                "age": age,
                "course": course
            }

            with open("students.csv", "a", newline="")as file:
                students = csv.writer(file)
                students.writerow([name, age, course])

    elif choice == "4":
        print("Auf weidersehn!")
        break

    else:
        print("Invalid choice!")

print("===================================================================")
