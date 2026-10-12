import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
course TEXT NOT NULL
)
""")

print("=================================================================")


while True:


    print("-----------------------------------------------------------------")
    print("\n1. Add students")
    print("2. View students")
    print("3. Search student")
    print("4. Update student's course")
    print("5. Delete student")
    print("6. Exit")
    print("-----------------------------------------------------------------")

    choice = input("Enter choice: ")
    
    if choice == "1":
        students_data = []
        number = int(input("Enter number of students to add: "))
        for i in range(number):
            print(f"\nstudent {i + 1}")
            name = input("Enter name of student: ").lower()
            age  = int(input("Enter age: "))
            course = input("Enter course: ").lower()
            students_data.append((name, age, course))

        cursor.executemany(
            "INSERT INTO students(name, age, course) VALUES(?, ?, ?)",
            students_data
        )
        connection.commit()

    elif choice == "2":
        cursor.execute(
            "SELECT * FROM students"
        )
        students = cursor.fetchall()
        for student in students:
            print(student)
    
        connection.commit()

    elif choice == "3":
        search_id= int(input("Enter student's id to search: "))

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (search_id,)
        )
        student = cursor.fetchone()

        if student:
            print("Student found!")
            print(f"ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Age: {student[2]}")
            print(f"Course: {student[3]}")

        else:
            print("Student not found!")

        connection.commit()

    elif choice == "4":
        student_id = int(input("Enter student's id: "))
        new_course = input("Enter new course: ").lower()

        cursor.execute(
            "UPDATE students SET course = ? WHERE id =?",
            (new_course, student_id)
        )
        if cursor.rowcount > 0:
            print("Course updated!")
        else:
            print("Student id not found!")

        connection.commit()

    elif choice == "5":
        student_id = int(input("Enter student id: "))

        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )
        if cursor.rowcount > 0:
            print("Student's records deleted successfully")
        else:
            print("Student's id not found!")

        connection.commit()

    elif choice == "6":
        print("Auf weidersehn!")
        break

    else:
        print("Invalid choice!")
connection.close()

print("================================================================")

