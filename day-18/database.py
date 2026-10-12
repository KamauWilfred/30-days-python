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

students_data = []

number = int(input("Enter number of students to add: "))
for i in range(number):
    print(f"\nstudent {i + 1}")

    name = input("Enter student's name: ").lower()
    age = int(input("Age: "))
    course = input("Course: ").lower()

    students_data.append((name, age, course))

cursor.executemany(
    "INSERT INTO students(name, age, course) VALUES(?, ?, ?)",
    students_data
)

cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
for student in students:
    print(student)

connection.commit()
connection.close()

student_id = int(input("Enter student's id: "))
new_course = input("Enter new course: ").lower()

cursor.execute(
    "UPDATE students SET course = ? WHERE id = ?",
    (new_course, student_id)
)

connection.commit()

if cursor.rowcount > 0:
    print("Student's course updated successfully!")
else:
    print("No student with such ID found!")

student_id = int("Enter student id to delete: ")
cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (student_id)
)
connection.commit()

if cursor.rowcount > 0:
    print("Student record deleted!")
else:
    print("No such student with that ID found!")
    